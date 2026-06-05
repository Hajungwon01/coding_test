SELECT
  name
FROM
  companies
WHERE
  company_id in (
    SELECT
      publisher_id
    FROM
      games
    GROUP BY
      publisher_id
    HAVING
      count(publisher_id) >= 10
  );