# Smag Grotto API

The API for Smag Grotto is served at [api.smag.lol](api.smag.lol).

Authorised routes, prefixed with a 🔐, require an additional parameter:
- <u>authentication</u>, type String(16), the auth string specific to the user

## Routes

### `GET /users`
#### Response 200
```js
{
	"users": [
		...UserObject(name, picture, bio)
	]
}
```
### 🔐 `POST /users`
#### Parameters
- <u>name</u>, type String(3, 32), the name of the user
- <u>picture</u>, type String(), a link to a picture
- <u>bio</u>, type String(3, 512), a short bio
#### Response 201
```js
{
	"message": "successfully added user"
}
```

```bash
*/5 * * * * /bin/cp data.json /var/backups/data.json
```