Rails.application.routes.draw do
  get '/v1/projects', to: 'projects#index'
end
