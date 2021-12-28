class GithubRepository

  class << self
    def fetch_all_issues(orgs, repos, token)
      conn = connection("https://api.github.com")
      res = conn.get "/repos/#{orgs}/#{repos}/issues" do |req|
        req.params[:per_page] = 10
        req.params[:page] = 1
        req.headers["Authorization"] = "token #{token}"
      end
      body = parse(res)
      GithubIssueList.new(body)
    end

    def connection(url)
      conn = Faraday.new(url: url)
    end

    def parse(res)
      JSON.parse(res.body)
    end
  end


end
