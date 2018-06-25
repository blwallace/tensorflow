## From https://bigquery.cloud.google.com/dataset/bigquery-public-data:ncaa_basketball?pli=1

SELECT
  ta.*,
  ta.wins - ta.losses as spread_0,
  tb.spread as spread_1,
  tc.spread as spread_2,
  td.spread as spread_3,
  te.spread as spread_4,
  tf.spread as spread_5

FROM
  [bigquery-public-data:ncaa_basketball.mbb_historical_teams_seasons] ta
JOIN (
  SELECT
    season + 1 AS js,
    season AS season,
    team_code AS team_code,
    wins - losses AS spread
  FROM
    [bigquery-public-data:ncaa_basketball.mbb_historical_teams_seasons] ) tb
ON
  ta.season = tb.js
  AND ta.team_code = tb.team_code
JOIN (
  SELECT
    season + 2 AS js,
    season AS season,
    team_code AS team_code,
    wins - losses AS spread
  FROM
    [bigquery-public-data:ncaa_basketball.mbb_historical_teams_seasons] ) tc
ON
  ta.season = tc.js
  AND ta.team_code = tc.team_code
JOIN (
  SELECT
    season + 3 AS js,
    season AS season,
    team_code AS team_code,
    wins - losses AS spread
  FROM
    [bigquery-public-data:ncaa_basketball.mbb_historical_teams_seasons] ) td
ON
  ta.season = td.js
  AND ta.team_code = td.team_code
JOIN (
  SELECT
    season + 4 AS js,
    season AS season,
    team_code AS team_code,
    wins - losses AS spread
  FROM
    [bigquery-public-data:ncaa_basketball.mbb_historical_teams_seasons] ) te
ON
  ta.season = te.js
  AND ta.team_code = te.team_code
JOIN (
  SELECT
    season + 5 AS js,
    season AS season,
    team_code AS team_code,
    wins - losses AS spread
  FROM
    [bigquery-public-data:ncaa_basketball.mbb_historical_teams_seasons] ) tf
ON
  ta.season = tf.js
  AND ta.team_code = tf.team_code
WHERE
  ta.division = 1
  AND ta.season = 2015