
### Migration

- 启动本地的mysql，推荐brew install
- create数据库：szse
- cd app && flask db init
- flask db migrate
- flask db upgrade


### 如果出现mysql插入不了中文：
```sql
ALTER TABLE szse.doc_type MODIFY COLUMN doc_type_desc text
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;
```

### 生成User-Info：
```python
import base64
import json
a = json.dumps({"app_id":1,"id":1,"username":"james","roles":[{"name": "管理员"}]})
b = a.encode("utf-8")
c = base64.b64encode(b)
print(c.decode("utf-8"))
```
Postman Header中增加:
`User-Info`: `eyJhcHBfaWQiOiAxLCAiaWQiOiAxLCAidXNlcm5hbWUiOiAiamFtZXMiLCAicm9sZXMiOiBbeyJuYW1lIjogIlx1N2JhMVx1NzQwNlx1NTQ1OCJ9XX0=`

