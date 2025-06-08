# Acquire the latest MathJax release and put it in the correct place.

rm -rf ./es5
git clone https://github.com/mathjax/MathJax.git ./mj-tmp
mv -f ./mj-tmp/es5 ./
rm -rf ./mj-tmp

# https://github.com/mathjax/MathJax/blob/master/README.md#reducing-the-size-of-the-components-directory
# Indeed, you should be able to remove everything other than ``tex-chtml.js``,
# and the ``input/tex/extensions``, ``output/chtml/fonts/woff-v2``, ``adaptors``, ``a11y``, and ``sre`` directories.
# If you are using the results only on the web, you can remove ``adaptors`` as well.

# If you are not using A11Y support (e.g., speech generation, or semantic enrichment),
# then you can remove a11y and sre as well
# (though in this case you may need to disable the assistive tools in the MathJax contextual menu
# in order to avoid MathJax trying to load them when they aren't there).

# Summary: keep just these:
# ./input/tex/extensions
# ./output/chtml/fonts/woff-v2
# ./tex-chtml.js
