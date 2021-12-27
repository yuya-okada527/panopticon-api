Rails.application.routes.draw do
  # Projects API
  get '/v1/projects', to: 'v1/projects#projects_get'

  # Tasks API
  get '/v1/projects/:project_id/tasks', to: 'v1/tasks#tasks_get'
  post '/v1/projects/:project_id/tasks', to:'v1/tasks#tasks_post'
  get '/v1/projects/:project_id/tasks/:task_id', to: 'v1/tasks#tasks_task_id_get'
  put '/v1/projects/:project_id/tasks/:task_id', to: 'v1/tasks#tasks_task_id_put'
  put '/v1/projects/:project_id/tasks/:task_id/status', to: 'v1/tasks#tasks_task_id_status_put'

  # TaskProviders API
  get '/v1/projects/:project_id/task_providers', to: 'v1/task_providers#task_providers_get'
  post '/v1/projects/:project_id/task_providers', to: 'v1/task_providers#task_providers_post'
  delete '/v1/projects/:project_id/task_providers/:task_provider_id', to: 'v1/task_providers#task_providers_task_provider_id_delete'
end
