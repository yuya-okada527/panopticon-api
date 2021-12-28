class GithubIssue

  #
  # number: Issue番号
  # title: Issue名
  # body: Issue概要
  # html_url: IssueのURL
  # state: Issueの状態
  # assignees: アサインされているユーザ名のリスト
  attr_accessor :number, :title, :body, :html_url, :state, :assignees

  def initialize(issue)
    self.number = issue["number"]
    self.title = issue["title"]
    self.body = issue["body"]
    self.html_url = issue["html_url"]
    self.state = issue["state"]
    self.assignees = issue["assignees"].map do |assignee|
      assignee["login"]
    end
  end
end
