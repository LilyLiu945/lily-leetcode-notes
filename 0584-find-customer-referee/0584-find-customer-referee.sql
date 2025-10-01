-- Equivalent solution using COALESCE:
-- In SQL, comparisons with NULL evaluate to UNKNOWN, so rows with NULL referee_id
-- would be excluded by `referee_id <> 2`. COALESCE(referee_id, 0) replaces NULL with
-- a non-2 sentinel (here 0), making a single comparison sufficient across dialects.
-- Note: wrapping the column in a function may limit index use depending on the engine.

SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) <> 2;