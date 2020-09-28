# Smag Grotto API

The API for Smag Grotto is served at [http://api.smag.lol](http://api.smag.lol).

Authorised routes, prefixed with a 🔐, require an additional parameter:
- <u>authentication</u>, type String(16), the auth string specific to the member

## Routes

### `GET /members`
#### Response 200
```js
{
	"members": [
		...MemberObject(name, picture, bio)
	]
}
```
### 🔐 `POST /members`
#### Parameters
- <u>name</u>, type String(3, 32), the name of the member
- <u>picture</u>, type String(), a link to a picture
- <u>bio</u>, type String(,512), a short bio
#### Response 201
```js
{
	"message": "successfully added member"
}
```