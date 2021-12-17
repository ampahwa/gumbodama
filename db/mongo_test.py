import pymongo as pm

client = pm.MongoClient()
print(f"{client=}")

insert_ret = client['gumbotdb']['some_collect'].insert_one({'fld': 'value'})
print(f"{insert_ret=}")

docs = client['gumbotdb']['some_collect'].find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")

doc = client['gumbotdb']['some_collect'].delete_one({'fld': 'value'})
print(f"find one = {doc=}")