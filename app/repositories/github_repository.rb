class GithubRepository

  class << self
    def fetch_all_issues(orgs, repos, token)
      conn = connection("https://api.github.com")
      github_issue_list = GithubIssueList.new
      page = 1
      while true do
        pp page
        res = conn.get "/repos/#{orgs}/#{repos}/issues" do |req|
          req.params[:per_page] = 30
          req.params[:page] = page
          req.headers["Authorization"] = "token #{token}"
        end
        body = parse(res)
        break if body.empty?
        github_issue_list.extend!(body)
        page += 1
        break if page > 10000 # 無限ループ予防
      end
      github_issue_list
    end

    def connection(url)
      conn = Faraday.new(url: url)
    end

    def parse(res)
      JSON.parse(res.body)
    end
  end


end
