function cleanForSlug(val, useURLify) {
    return val.replace(/[^A-Za-z0-9\0080-\uFFFF\-\s]/g, '').trim().replace(/[\!\@\#\$\%\^\&\*\(\)\{\}\:\;\"\'\,\.\/\?\+\<\>]/g,'').replace(/\s+/g, '-').toLowerCase();
}
