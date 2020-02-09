from content_checker import create_app, config
import pytest


@pytest.fixture
def app():
    return create_app(config=config.Testing)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    from content_checker import db
    from content_checker.models import User, Task, ContentIntegratedLab

    with app.app_context():
        db.create_all()
        for user in ["ben", "john", "peter"]:
            db.session.add(User(username=user))

        for instruction, answer in zip(
            ["Who?", "What?", "When?"], ["answer who", "answer what", "answer when"]
        ):
            db.session.add(Task(instruction=instruction, answer=answer))

        db.session.commit()

        for user in User.query.all():
            for task in Task.query.all():
                db.session.add(
                    ContentIntegratedLab(
                        user=user, task=task, user_answer=None, score=0
                    )
                )

        db.session.commit()
        yield db
        db.drop_all()
        db.session.commit()


@pytest.mark.parametrize("client, result", [(None, True)], indirect=["client"])
def test_create_fdb(client, result):
    expected = {
        "user_answer": "",
        "expected": "",
        "result": result,
    }
    response = client.post("/content/create_fdb", data=dict(username="testuser"))
    assert response.get_json() == expected


# def test_extract_files(client):
#     response = client.post("/content/extract_files", data=dict(username="testuser"))


# def test_transform_files(client):
#     response = client.post("/content/transform_files", data=dict(username="testuser"))


# def test_load(client):
#     response = client.post("/content/load", data=dict(username="testuser"))


# def test_create_worflow(client):
#     response = client.post("/content/create_worflow", data=dict(username="testuser"))


# def test_run_worflow(client):
#     response = client.post("/content/run_worflow", data=dict(username="testuser"))


# def test_fdb_add_field_shares(client):
#     response = client.post(
#         "/content/fdb_add_field_shares", data=dict(username="testuser")
#     )


# def test_fdb_add_field_mcap(client):
#     response = client.post(
#         "/content/fdb_add_field_mcap", data=dict(username="testuser")
#     )


# def test_fdb_shares_mcap_data_check(client):
#     response = client.post(
#         "/content/fdb_shares_mcap_data_check", data=dict(username="testuser")
#     )
