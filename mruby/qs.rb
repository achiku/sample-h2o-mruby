class QueryStringApp
  def call(env)
    query = env["QUERY_STRING"]
    [
      200,
      {
        "content-type" => "text/plain; charset=utf-8"
      },
      [query]
    ]
  end
end

QueryStringApp.new
