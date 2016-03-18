function cleanForSlug(val, useURLify) {
    // Inspired from http://www.andornot.com/blog/post/Replace-MS-Word-special-characters-in-javascript-and-C.aspx
    return val.replace(/[^A-Za-z0-9\0080-\uFFFF\-\s]/g, '').trim()
	.replace(/[\!\@\#\$\%\^\&\*\(\)\{\}\:\;\"\'\,\.\/\?\+\<\>]/g,'')
	.replace(/\s+/g, '-')
        // smart single quotes and apostrophe
	.replace(/[\u2018\u2019\u201A]/g, "")
	// smart double quotes
	.replace(/[\u201C\u201D\u201E]/g, "")
	// ellipsis
	.replace(/\u2026/g, "...")
        // dashes
	.replace(/[\u2013\u2014]/g, "-")
	// circumflex
	.replace(/\u02C6/g, "^")
	// open angle bracket
	.replace(/\u2039/g, "<")
        // close angle bracket
	.replace(/\u203A/g, ">")
        // spaces
	.replace(/[\u02DC\u00A0]/g, " ")
	.toLowerCase();
}
