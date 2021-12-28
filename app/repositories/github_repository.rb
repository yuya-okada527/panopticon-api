class GithubRepository

  class << self
    def fetch_all_issues(base_url, token)
      conn = connection("https://api.github.com/repos/yuya-okada527/panopticon-api")
      res = conn.get '/issues' do |req|
        req.params[:per_page] = 10
        req.params[:page] = 1
        req.headers["Authorization"] = "token #{token}"
      end
      JSON.parse(res.body)
    end

    def connection(url)
      conn = Faraday.new(url: url)
    end
  end


end
