# sqlalchemy_py3web
sqlalchemy plugin for py3web

## how to use
```
    from sqlalchemy_plugin import plugin
    plugin.init()
    app.add_processor(plugin.processor)
```

## config list
```
database:
    protocol: 'mysql+mysqlconnector'
    username: 'root'
    password: 'the_password'
    host: 'localhost'
    port: 3306
    database: 'database_name'
```

## examples:
`pass`