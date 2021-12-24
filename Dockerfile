FROM ruby:3.0.1

ENV APP_ROOT="/app" \
		LANG=C.UTF-8	\
		TZ=Asia/Tokyo

WORKDIR $APP_ROOT

RUN apt-get update -qq \
	&& apt-get install -y \
  	build-essential \
		libpq-dev \
		nodejs \
		default-mysql-client \
		vim \
		curl \
	&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
	&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
	&& apt-get update \
	&& apt-get install -y yarn

COPY Gemfile* $APP_ROOT/

RUN bundle install

COPY . $APP_ROOT/
