SELECT DISTINCT page_location
FROM ga
WHERE instr(page_location, '_') = 0
ORDER BY page_location;