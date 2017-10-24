SELECT
	title
FROM
	xxx_title_class
WHERE
	(
		title REGEXP '[abcdefghijklmnopqrstuvwxyz]c.o'
	)

========================================================================
SELECT
	title
FROM
	xxx_title_class
WHERE
	title NOT REGEXP '[^0-9.]'