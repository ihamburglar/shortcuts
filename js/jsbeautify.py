import jsbeautifier
opts = jsbeautifier.default_options()
opts.indent_size = 4
res = jsbeautifier.beautify_file('E-v1.js', opts)
#res = jsbeautifier.beautify('your javascript string')
#res = jsbeautifier.beautify_file('some_file.js')
print(res)
