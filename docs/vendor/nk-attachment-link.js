/**
 * 附件下载链接修正（vendor/nk-attachment-link.js）
 * --------------------------------------------------------------
 * 问题：docsify 会把指向 .xlsx/.docx/.pdf 等附件的相对链接也编译成 hash 路由
 *       （#/04_chuangye/带货/xxx.xlsx），点击时被当作页面去加载同名 .md，
 *       于是显示 404。托管层又要求每个资源请求都带 sharecode 参数。
 *
 * 做法：每次渲染完成后，把这类链接还原为真实文件地址（相对 docs 根解析成
 *       绝对 URL），把当前页面 URL 上的分享参数（如 sharecode）自动附加，
 *       并加 download 属性让浏览器直接下载。
 *
 * md 源文件继续写相对 docs 根的路径即可，不必硬编码域名或凭证。
 * 双入口（index.html / alumni.html）共用本文件。
 */
(function () {
  var ATTACH = /\.(xlsx|xls|docx|doc|pptx|ppt|pdf|zip|csv|7z|rar)(\?|#|$)/i;

  function normalize(href) {
    // 去掉 docsify 加的 hash 路由前缀（#/ 或 #）
    var rel = href.replace(/^#\/?/, '');
    // 只保留路径部分，丢掉可能已有的 query / hash
    rel = rel.split(/[?#]/)[0];
    if (!rel) return null;

    // 相对 docs 根：以当前文档所在目录为基准解析
    var base = location.origin + location.pathname;
    var u;
    try { u = new URL(rel, base); } catch (e) { return null; }

    // 把当前页面的分享参数（sharecode 等）附加过去；已有同名参数不覆盖
    var cur = new URLSearchParams(location.search);
    cur.forEach(function (v, k) {
      if (!u.searchParams.has(k)) u.searchParams.set(k, v);
    });
    return u.toString();
  }

  function fix() {
    var scope = document.querySelector('.markdown-section') || document;
    var links = scope.querySelectorAll('a[href]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var href = a.getAttribute('href') || '';
      if (!ATTACH.test(href)) continue;
      var url = normalize(href);
      if (!url) continue;
      a.setAttribute('href', url);
      a.setAttribute('download', '');
    }
  }

  function plugin(hook) {
    hook.doneEach(fix);
  }

  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (window.$docsify.plugins || []).concat([plugin]);
})();
