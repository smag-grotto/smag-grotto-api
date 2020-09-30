# Smag Grotto API

The API for Smag Grotto is served at [http://api.smag.lol](http://api.smag.lol).

Authorised routes, prefixed with a 🔐, require an additional parameter:
- <u>authentication</u>, type String(16), the auth string specific to the member

## Preview Routes

#### `GET /members` - return all members
#### `POST /members` - create new member
#### `GET /members/<member>` - get a member
#### TODO `PATCH /members/<member>` - edit a member

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
- <u>[bio]</u>, type String(,512), a short bio
#### Response 201
```js
{
	"message": "successfully added member"
}
```

#### To do

- Add restrictions to only allow authorised requests
- Add restrictions to only allow certain parameters to be posted

### `GET /members/<member>`
#### Response 200
```js
{
	MemberObject(name, picture, bio)
}
```

### `PATCH /members/<member>`
#### Parameters
- <u>[name]</u>, type String(3, 32), the name of the member
- <u>[picture]</u>, type String(), a link to a picture
- <u>[bio]</u>, type String(,512), a short bio
#### Response 200
```js
{
	"message": "successfully edited member"
}
```