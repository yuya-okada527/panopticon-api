Rails.application.routes.draw do
  get '/v1/projects', to: 'v1/projects#index'
end
