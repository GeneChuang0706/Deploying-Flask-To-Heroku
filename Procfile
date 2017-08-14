web: bundle exec rails server -p $PORT
web: lein run -m gunicorn $PORT
web: sh target/bin/app_run1
worker:  bundle exec rake jobs:work

web gunicorn app_run1:app
