from activities import app, config

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.get('app').get('port'))
