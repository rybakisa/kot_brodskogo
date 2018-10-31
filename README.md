# kot_brodskogo

## Requirements

 * Python `.python-version`
 * Node.js `.nvmrc`
 * Yarn `.yvmrc`

## Install

1. Initialize project

```sh
cp .env.example .env
cp .env-dev.example .env-dev
./install.sh
```

This will initialize backend and build frontend

2. Run server

```
python manage.py runserver
```

This will launch Python builtin web server to interact scripts with database and navigate through routes.

3. Open server URL from terminal in browser
4. Navigate to `/admin` and login with `admin` username with `admin` password

## Update

```sh
./update.sh
```
