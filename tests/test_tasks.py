def test_tasks_crud(client, token):
    h = {"Authorization": f"Bearer {token}"}
    # create
    r1 = client.post("/tasks/", json={"title":"Task1","description":"d"}, headers=h)
    assert r1.status_code == 201
    tid = r1.json()["id"]
    # list
    r2 = client.get("/tasks/", headers=h); assert r2.status_code == 200; assert len(r2.json()) == 1
    # get
    r3 = client.get(f"/tasks/{tid}", headers=h); assert r3.status_code == 200
    # update
    r4 = client.put(f"/tasks/{tid}", json={"title":"T1 updated","description":"d2"}, headers=h)
    assert r4.status_code == 200 and r4.json()["title"] == "T1 updated"
    # delete
    r5 = client.delete(f"/tasks/{tid}", headers=h); assert r5.status_code == 204
    r6 = client.get("/tasks/", headers=h); assert r6.status_code == 200 and r6.json() == []

