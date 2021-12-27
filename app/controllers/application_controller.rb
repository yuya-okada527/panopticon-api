class ApplicationController < ActionController::Base
  # TODO セキュリティ関連
  protect_from_forgery with: :null_session
end
