from activities import app, config

if __name__ == '__main__':
    app.run(port=config.get('app').get('port'))
