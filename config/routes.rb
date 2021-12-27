Rails.application.routes.draw do
  get '/v1/projects', to: 'v1/projects#projects_get'
end
