Rails.application.routes.draw do
  namespace :v1, format: 'json' do
    resources :projects, only: [:index]
  end
end
