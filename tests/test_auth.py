def test_signup_login_flow(client):
    r1 = client.post("/auth/signup", json={"email":"u1@example.com","password":"pass"})
    assert r1.status_code == 201
    r2 = client.post("/auth/signup", json={"email":"u1@example.com","password":"pass"})
    assert r2.status_code == 400  # duplicate
    r3 = client.post("/auth/login",
        data={"username":"u1@example.com","password":"pass"},
        headers={"Content-Type":"application/x-www-form-urlencoded"})
    assert r3.status_code == 200
    assert "access_token" in r3.json()

