Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
import urllib2

 

>>> page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
>>> try:
	request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
  File "<pyshell#3>", line 4
    response = urllib2.urlopen(request)
                                      ^
IndentationError: unindent does not match any outer indentation level
>>> 
>>> 

line 373, in _read_status
 raise BadStatusLine(line)
httplib.BadStatusLine: ''
1
2
3
line 373, in _read_status
 raise BadStatusLine(line)
httplib.BadStatusLine: ''
SyntaxError: invalid syntax
>>> 
>>> import urllib
>>> import urllib2
>>> page = 1
>>> url = 'http://www.qiushibaike.com/hot/page/' + str(page)
>>> user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
>>> headers = { 'User-Agent' : user_agent }
>>> try:
	request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
  File "<pyshell#14>", line 4
    response = urllib2.urlopen(request)
                                      ^
IndentationError: unindent does not match any outer indentation level
>>> request = urllib2.Request(url,headers = headers)
>>> response = urllib2.urlopen(request)
>>> print response.read()
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta http-equiv="X-UA-Compatible" content="chrome=1,IE=edge">
<meta name="renderer" content="webkit"/>
<meta name="applicable-device" content="pc">


















<title>24小时爆笑笑话大全 - 糗事百科</title>






















<meta name="keywords" content="笑话,笑话大全" />
<meta name="description" content="糗事百科官网提供24小时最糗搞笑笑话大全,糗百24小时内最新最糗事就只在糗事百科官网24小时专题,囊括恶搞、最尴尬糗事精华,快乐减压！"/>
<meta http-equiv="mobile-agent" content="format=xhtml;url=//www.qiushibaike.com/hot/">
<meta http-equiv="mobile-agent" content="format=html5;url=//www.qiushibaike.com/hot/">



<meta name="robots" content="noarchive">
<link href="//static.qiushibaike.com/css/dist/web/app.min.css?v=fd76de5efd22f0f804665ba809048729" media="screen, projection" rel="stylesheet" type="text/css"/>
<script type="text/javascript">
// Baidu Automatic push content
var _hmt = _hmt || [];
(function() {
var hm = document.createElement("script");
hm.src = "https://hm.baidu.com/hm.js?2670efbdd59c7e3ed3749b458cafaa37";
var s = document.getElementsByTagName("script")[0];
s.parentNode.insertBefore(hm, s);
})();
// 收集运营上缓存证据
window.config = {
'user_time': '2017-11-20 10:35:25',
'version': '2017-09-04 14:36'
}
</script>
</head>
<body>



<div id="header" class="head">
<div class="content-block">
<div class="logo" id="hd_logo">
<a href="/"><h1>糗事百科</h1></a>
</div>
<div id="menu" class="menu-bar menu clearfix" style="margin:0 10px">
<a  href="/" rel="nofollow">热门</a>
<a  id="highlight"  href="/hot/">24小时</a>
<a  href="/imgrank/">热图</a>
<a  href="/text/">文字</a>
<a  href="/history/">穿越</a>
<a  href="/pic/">糗图</a>
<a  href="/textnew/">新鲜</a>
<a  class="fn-signin-required" href="javascript:void(0);" data-go="/article/add" rel="nofollow">投稿</a>
<!--<a href="http://www.youliaodao.cn" target="_blank" rel="nofollow">百科</a>-->
</div>
<div class="userbar clearfix">
<div class="login hidden">
<a href="/my" class="username" id="uname" rel="nofollow"></a>
</div>
<div class="logout">
<a href="javascript:void(0);" class="fn-signin-required logintop" id='logintop' rel="nofollow" style="font-size:16.5px;">登录</a>
</div>
</div>
</div>
</div>



<div id="content" class="main">
<div class="content-block clearfix">

<div id="content-left" class="col1">








<div class="article block untagged mb15 typs_long" id='qiushi_tag_119742381'>


<div class="author clearfix">
<span style="height: 35px">
<img src="//static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="匿名用户">
</span>
<span>
<h2>匿名用户</h2>
</span>
<!-- <div class="articleGender manIcon">32</div> -->
</div>

<a href="/article/119742381" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


不算糗事，但是让我很感慨，今年28，结婚生了孩子，当年因为有了孩子还没车，特别麻烦，我家到老婆家没有车，后来贷款5万买了个二手车代步，最近几天到期需要周转一下，问了我哥，几个关系很好的朋友，知道他们有，但是开口都说没有，只能向一个关系一般般，但是比较好说话的朋友开口，二话不说就转给我了，而且还是他给员工发工资的钱，只跟我说他发工资前还他就好！为了这事奔波了很久，挺感谢他的！经常听人说朋友不需要多，有一个靠谱的就够了！非常感谢他！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">566</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119742381" data-share="/article/119742381" id="c-119742381" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">49</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119742381" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119742381" class="up">
<a href="javascript:voting(119742381,1)" class="voting" data-article="119742381" id="up-119742381" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">578</span>
</a>
</li>
<li id="vote-dn-119742381" class="down">
<a href="javascript:voting(119742381,-1)" class="voting" data-article="119742381" id="dn-119742381" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/119742381" id="c-119742381" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764926'>


<div class="author clearfix">
<a href="/users/30107945/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3010/30107945/thumb/20171111121842.JPEG?imageView2/1/w/90/h/90" alt="流浪的猫*">
</a>
<a href="/users/30107945/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
流浪的猫*
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/119764926" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


期中考试成绩下来了，我正打电话训孩子，让他今晚等着瞧。<br/>厂里刚进口的德国造设备又报.警了，整个车间警笛大作。<br/>“爸爸...爸爸...”电话那头传来颤抖的声音...“你被警.察包围了？你今晚回不来了对吗？...噢~耶……”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">960</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119764926" data-share="/article/119764926" id="c-119764926" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">15</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119764926" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764926" class="up">
<a href="javascript:voting(119764926,1)" class="voting" data-article="119764926" id="up-119764926" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">977</span>
</a>
</li>
<li id="vote-dn-119764926" class="down">
<a href="javascript:voting(119764926,-1)" class="voting" data-article="119764926" id="dn-119764926" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119764926" id="c-119764926" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119764926" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">醉酒舞剑砍疯子※：</span>
<div class="main-text">
楼主你就招了吧，说，这是第几次 嫖 娼
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


15

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119765011'>


<div class="author clearfix">
<a href="/users/5018907/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/501/5018907/thumb/20171119214649.JPEG?imageView2/1/w/90/h/90" alt="雪七七...">
</a>
<a href="/users/5018907/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
雪七七...
</h2>
</a>
<div class="articleGender womenIcon">30</div>
</div>

<a href="/article/119765011" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


儿子喜欢玩妖怪抓唐僧的游戏，每次都是儿子演悟空，老公演唐僧，我演妖怪。<br/>昨天，我不干了，我要演唐僧......<br/>儿子威风凛凛，正襟危坐：“孩儿们，把唐僧给我押上来；混蛋，没有我的命令，谁把他烤了，还烤焦了”<br/><br/>小兔崽子......老娘有那么黑吗？

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1073</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119765011" data-share="/article/119765011" id="c-119765011" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">30</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119765011" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119765011" class="up">
<a href="javascript:voting(119765011,1)" class="voting" data-article="119765011" id="up-119765011" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1091</span>
</a>
</li>
<li id="vote-dn-119765011" class="down">
<a href="javascript:voting(119765011,-1)" class="voting" data-article="119765011" id="dn-119765011" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-18</span>
</a>
</li>
<li class="comments">
<a href="/article/119765011" id="c-119765011" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119750485'>


<div class="author clearfix">
<a href="/users/33694723/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3369/33694723/thumb/20171110211954.JPEG?imageView2/1/w/90/h/90" alt="感情会员">
</a>
<a href="/users/33694723/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
感情会员
</h2>
</a>
<div class="articleGender manIcon">44</div>
</div>

<a href="/article/119750485" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


今上午，老婆大喊：哎！老公咱家的锅漏了！<br/>奥！我说，你老抱怨早上我烧的米汤像米饭！<br/>原来不怪我添水少啊！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2296</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119750485" data-share="/article/119750485" id="c-119750485" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119750485" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119750485" class="up">
<a href="javascript:voting(119750485,1)" class="voting" data-article="119750485" id="up-119750485" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2327</span>
</a>
</li>
<li id="vote-dn-119750485" class="down">
<a href="javascript:voting(119750485,-1)" class="voting" data-article="119750485" id="dn-119750485" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-31</span>
</a>
</li>
<li class="comments">
<a href="/article/119750485" id="c-119750485" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119750485" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">江山未老红颜旧：</span>
<div class="main-text">
漏出来的水都进了楼主的脑袋～～～
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


11

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809241'>


<div class="author clearfix">
<a href="/users/12433067/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1243/12433067/thumb/20170608174016.JPEG?imageView2/1/w/90/h/90" alt="大吊一甩威震四海">
</a>
<a href="/users/12433067/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
大吊一甩威震四海
</h2>
</a>
<div class="articleGender manIcon">30</div>
</div>

<a href="/article/118809241" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


真事不割，留着有用…楼主经营一家小饭馆，隔壁是家面店。这是背景。有天三岁儿子过去玩，看见隔壁老板在洗碗。就问到:叔叔，怎么是你在洗碗呀，阿姨怎么不洗。瞬间感觉隔壁老板受到了10000点真实伤害…

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">746</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/118809241" data-share="/article/118809241" id="c-118809241" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">2</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_118809241" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809241" class="up">
<a href="javascript:voting(118809241,1)" class="voting" data-article="118809241" id="up-118809241" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">769</span>
</a>
</li>
<li id="vote-dn-118809241" class="down">
<a href="javascript:voting(118809241,-1)" class="voting" data-article="118809241" id="dn-118809241" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-23</span>
</a>
</li>
<li class="comments">
<a href="/article/118809241" id="c-118809241" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119759386'>


<div class="author clearfix">
<a href="/users/33373264/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3337/33373264/thumb/20171004220626.JPEG?imageView2/1/w/90/h/90" alt="别闹baby">
</a>
<a href="/users/33373264/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
别闹baby
</h2>
</a>
<div class="articleGender womenIcon">18</div>
</div>

<a href="/article/119759386" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


灵感源于生活。

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/119759386" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11975/119759386/medium/app119759386.jpg" alt="糗事#119759386" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1329</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119759386" data-share="/article/119759386" id="c-119759386" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">10</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119759386" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119759386" class="up">
<a href="javascript:voting(119759386,1)" class="voting" data-article="119759386" id="up-119759386" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1364</span>
</a>
</li>
<li id="vote-dn-119759386" class="down">
<a href="javascript:voting(119759386,-1)" class="voting" data-article="119759386" id="dn-119759386" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-35</span>
</a>
</li>
<li class="comments">
<a href="/article/119759386" id="c-119759386" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119759386" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">WAJJ一笑而过：</span>
<div class="main-text">
又高于生活
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


6

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764743'>


<div class="author clearfix">
<a href="/users/10904125/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1090/10904125/thumb/20140711122500.jpg?imageView2/1/w/90/h/90" alt="望起脑壳跑">
</a>
<a href="/users/10904125/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
望起脑壳跑
</h2>
</a>
<div class="articleGender manIcon">23</div>
</div>

<a href="/article/119764743" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


今天23岁生日，给自己许个愿吧。如果过5000赞就去广东把前女友和她儿子一起接回来（14年分手的。她结婚后又离了，我至今一直单身）  坚决不匿

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1810</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119764743" data-share="/article/119764743" id="c-119764743" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">46</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119764743" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764743" class="up">
<a href="javascript:voting(119764743,1)" class="voting" data-article="119764743" id="up-119764743" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1873</span>
</a>
</li>
<li id="vote-dn-119764743" class="down">
<a href="javascript:voting(119764743,-1)" class="voting" data-article="119764743" id="dn-119764743" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-63</span>
</a>
</li>
<li class="comments">
<a href="/article/119764743" id="c-119764743" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119764743" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">夜很长……心很凉！：</span>
<div class="main-text">
不想接就不接，还5千赞？？想接现在都接回来了…一天天的，自己心里到底怎么想的没点逼数啊！！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


24

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764704'>


<div class="author clearfix">
<a href="/users/25268858/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2526/25268858/thumb/20171103055534.JPEG?imageView2/1/w/90/h/90" alt="小语の礼物">
</a>
<a href="/users/25268858/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
小语の礼物
</h2>
</a>
<div class="articleGender womenIcon">23</div>
</div>

<a href="/article/119764704" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


晚间散步，老公走在最前面，然后突然停下来，正准备问他怎么停下来时，只听见噗的一声，放了个响屁，然后若无其事地继续往前走。。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">900</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119764704" data-share="/article/119764704" id="c-119764704" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">9</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119764704" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764704" class="up">
<a href="javascript:voting(119764704,1)" class="voting" data-article="119764704" id="up-119764704" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">912</span>
</a>
</li>
<li id="vote-dn-119764704" class="down">
<a href="javascript:voting(119764704,-1)" class="voting" data-article="119764704" id="dn-119764704" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-12</span>
</a>
</li>
<li class="comments">
<a href="/article/119764704" id="c-119764704" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119764906'>


<div class="author clearfix">
<a href="/users/34246786/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3424/34246786/thumb/20171101204316.JPEG?imageView2/1/w/90/h/90" alt="老巫婆～～">
</a>
<a href="/users/34246786/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
老巫婆～～
</h2>
</a>
<div class="articleGender womenIcon">12</div>
</div>

<a href="/article/119764906" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


一个年轻的爸爸把儿子放在脖子上逛商场。商场突然放起了节奏感很强的音乐，儿子就抓着爸爸的头发跟着音乐扭动小身板，被抓头发的爸爸一脸纠结痛苦又忍耐的任儿子舞动头发～

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1101</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119764906" data-share="/article/119764906" id="c-119764906" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119764906" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119764906" class="up">
<a href="javascript:voting(119764906,1)" class="voting" data-article="119764906" id="up-119764906" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1118</span>
</a>
</li>
<li id="vote-dn-119764906" class="down">
<a href="javascript:voting(119764906,-1)" class="voting" data-article="119764906" id="dn-119764906" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119764906" id="c-119764906" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809005'>


<div class="author clearfix">
<a href="/users/30016699/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3001/30016699/thumb/20170331001525.JPEG?imageView2/1/w/90/h/90" alt="Sn笑工坊">
</a>
<a href="/users/30016699/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
Sn笑工坊
</h2>
</a>
<div class="articleGender manIcon">24</div>
</div>

<a href="/article/118809005" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


有木有火云邪神小时候的感觉呢？

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/118809005" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11880/118809005/medium/app118809005.jpg" alt="糗事#118809005" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">552</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/118809005" data-share="/article/118809005" id="c-118809005" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">6</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_118809005" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809005" class="up">
<a href="javascript:voting(118809005,1)" class="voting" data-article="118809005" id="up-118809005" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">566</span>
</a>
</li>
<li id="vote-dn-118809005" class="down">
<a href="javascript:voting(118809005,-1)" class="voting" data-article="118809005" id="dn-118809005" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-14</span>
</a>
</li>
<li class="comments">
<a href="/article/118809005" id="c-118809005" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119765072'>


<div class="author clearfix">
<a href="/users/23331917/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2333/23331917/thumb/2017111618530749.JPEG?imageView2/1/w/90/h/90" alt="36D※傻晴°">
</a>
<a href="/users/23331917/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
36D※傻晴°
</h2>
</a>
<div class="articleGender womenIcon">25</div>
</div>

<a href="/article/119765072" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


下午得罪了男同事，赶紧求饶道:我错了你原谅我吧！<br/>男同事黑着脸说:原谅你可以，除非你陪我睡一觉！<br/>当时脑袋一抽说道:还有这种好事？？<br/>麻蛋……你们都别这样看着我啊……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">895</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119765072" data-share="/article/119765072" id="c-119765072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">41</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119765072" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119765072" class="up">
<a href="javascript:voting(119765072,1)" class="voting" data-article="119765072" id="up-119765072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">912</span>
</a>
</li>
<li id="vote-dn-119765072" class="down">
<a href="javascript:voting(119765072,-1)" class="voting" data-article="119765072" id="dn-119765072" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119765072" id="c-119765072" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119765072" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">青刺莓：</span>
<div class="main-text">
男同事激动的语无伦次，还……还有……还有这种……还有这种好事?！
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


23

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762249'>


<div class="author clearfix">
<a href="/users/20115333/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2011/20115333/thumb/2017111200131222.JPEG?imageView2/1/w/90/h/90" alt="巾帼英雄小木兰">
</a>
<a href="/users/20115333/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
巾帼英雄小木兰
</h2>
</a>
<div class="articleGender womenIcon">68</div>
</div>

<a href="/article/119762249" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


周末我爸妈说请我吃大餐。菜一上，我立刻开启风卷残云模式，我爸环顾四周，顶着旁人看大猩猩的眼神轻声说:你这饿鬼似的吃相丢了我和你妈一样东西！我问:什么？我爸:脸……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1177</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762249" data-share="/article/119762249" id="c-119762249" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">14</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762249" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762249" class="up">
<a href="javascript:voting(119762249,1)" class="voting" data-article="119762249" id="up-119762249" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1194</span>
</a>
</li>
<li id="vote-dn-119762249" class="down">
<a href="javascript:voting(119762249,-1)" class="voting" data-article="119762249" id="dn-119762249" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-17</span>
</a>
</li>
<li class="comments">
<a href="/article/119762249" id="c-119762249" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762249" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
快把盘子放下！那个不能吃！咯牙，，[捂脸]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


7

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119745840'>


<div class="author clearfix">
<a href="/users/31017736/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3101/31017736/thumb/20160124002717.jpg?imageView2/1/w/90/h/90" alt="918疯狂英子">
</a>
<a href="/users/31017736/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
918疯狂英子
</h2>
</a>
<div class="articleGender womenIcon">36</div>
</div>

<a href="/article/119745840" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


各位糗友，如果流鼻血了，千万不要躺着不要问我为什么。整个鼻腔都是半凝固的血。去厕所吐了一大口血。把我爸吓得穿着睡衣抓起车钥匙想把我抱着走。结果没抱动。。没抱动。。。动。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3630</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119745840" data-share="/article/119745840" id="c-119745840" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">66</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119745840" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119745840" class="up">
<a href="javascript:voting(119745840,1)" class="voting" data-article="119745840" id="up-119745840" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3673</span>
</a>
</li>
<li id="vote-dn-119745840" class="down">
<a href="javascript:voting(119745840,-1)" class="voting" data-article="119745840" id="dn-119745840" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-43</span>
</a>
</li>
<li class="comments">
<a href="/article/119745840" id="c-119745840" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762767'>


<div class="author clearfix">
<a href="/users/22085995/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2208/22085995/thumb/2017111622015739.JPEG?imageView2/1/w/90/h/90" alt="（驹迷）真的爱你">
</a>
<a href="/users/22085995/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
（驹迷）真的爱你
</h2>
</a>
<div class="articleGender manIcon">18</div>
</div>

<a href="/article/119762767" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


班主任课，翔意来袭，不好意思在他课去<br/>忽然他手机响了，说有事，让大家自习<br/>等班主任一走，我也出去，谁知道，他把门从外面锁了……

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2969</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762767" data-share="/article/119762767" id="c-119762767" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">34</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762767" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762767" class="up">
<a href="javascript:voting(119762767,1)" class="voting" data-article="119762767" id="up-119762767" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2997</span>
</a>
</li>
<li id="vote-dn-119762767" class="down">
<a href="javascript:voting(119762767,-1)" class="voting" data-article="119762767" id="dn-119762767" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-28</span>
</a>
</li>
<li class="comments">
<a href="/article/119762767" id="c-119762767" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762767" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">胖香：</span>
<div class="main-text">
拉干的还好说，能兜的住，拉稀的咋整？[捂脸]
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


35

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809922'>


<div class="author clearfix">
<a href="/users/26728684/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/2672/26728684/thumb/20150318174320.jpg?imageView2/1/w/90/h/90" alt="什么名是没注册的">
</a>
<a href="/users/26728684/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
什么名是没注册的
</h2>
</a>
<div class="articleGender manIcon">32</div>
</div>

<a href="/article/118809922" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


昨晚下大雨，给同城买家送茶叶，约好买家小区门口等，快到的时候我问他，在哪里？<br/>他说：全家门口等<br/>我忙说：下那么大雨，不用全家来的<br/>他说：全家是便利店<br/>我：。。。。。。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3727</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/118809922" data-share="/article/118809922" id="c-118809922" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">26</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_118809922" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809922" class="up">
<a href="javascript:voting(118809922,1)" class="voting" data-article="118809922" id="up-118809922" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3801</span>
</a>
</li>
<li id="vote-dn-118809922" class="down">
<a href="javascript:voting(118809922,-1)" class="voting" data-article="118809922" id="dn-118809922" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-74</span>
</a>
</li>
<li class="comments">
<a href="/article/118809922" id="c-118809922" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119763193'>


<div class="author clearfix">
<a href="/users/33922427/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3392/33922427/thumb/20170622234817.JPEG?imageView2/1/w/90/h/90" alt="坤朋9">
</a>
<a href="/users/33922427/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
坤朋9
</h2>
</a>
<div class="articleGender manIcon">0</div>
</div>

<a href="/article/119763193" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


谁有过这样的经历。去办身份证的时候，名字被换成了同音的字，与之前毕业证上的名字不一样了。我，我父亲，我母亲身份证上的名字都被写错了，从此将错就错了，只是有时候办事还得去单位开证明，证明曾用名是某某某。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">816</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119763193" data-share="/article/119763193" id="c-119763193" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">17</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119763193" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119763193" class="up">
<a href="javascript:voting(119763193,1)" class="voting" data-article="119763193" id="up-119763193" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">827</span>
</a>
</li>
<li id="vote-dn-119763193" class="down">
<a href="javascript:voting(119763193,-1)" class="voting" data-article="119763193" id="dn-119763193" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-11</span>
</a>
</li>
<li class="comments">
<a href="/article/119763193" id="c-119763193" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762101'>


<div class="author clearfix">
<a href="/users/33694723/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3369/33694723/thumb/20171110211954.JPEG?imageView2/1/w/90/h/90" alt="感情会员">
</a>
<a href="/users/33694723/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
感情会员
</h2>
</a>
<div class="articleGender manIcon">44</div>
</div>

<a href="/article/119762101" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


小时候听人说，七夕的晚上嘴里含着馿屎蛋子，藏在紫茄子菜园里，到夜深人静就能听到牛郎织女的说话声。<br/>那时真想听听仙女说话，我就照做了，躲在菜园里等啊等，最后睡着了。<br/>醒来时，嘴里满是馿粪沫子，一脸迷茫地擦擦嘴回家了！<br/>长大了才知道是哄小孩子的！

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1794</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762101" data-share="/article/119762101" id="c-119762101" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">35</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762101" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762101" class="up">
<a href="javascript:voting(119762101,1)" class="voting" data-article="119762101" id="up-119762101" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1815</span>
</a>
</li>
<li id="vote-dn-119762101" class="down">
<a href="javascript:voting(119762101,-1)" class="voting" data-article="119762101" id="dn-119762101" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-21</span>
</a>
</li>
<li class="comments">
<a href="/article/119762101" id="c-119762101" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119763035'>


<div class="author clearfix">
<span style="height: 35px">
<img src="//static.qiushibaike.com/images/thumb/anony.png?v=b61e7f5162d14b7c0d5f419cd6649c87" alt="匿名用户">
</span>
<span>
<h2>匿名用户</h2>
</span>
<!-- <div class="articleGender manIcon">32</div> -->
</div>

<a href="/article/119763035" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


确实是这个理。。你们都是哪里的？

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/119763035" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11976/119763035/medium/app119763035.jpg" alt="糗事#119763035" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1425</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119763035" data-share="/article/119763035" id="c-119763035" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">48</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119763035" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119763035" class="up">
<a href="javascript:voting(119763035,1)" class="voting" data-article="119763035" id="up-119763035" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1476</span>
</a>
</li>
<li id="vote-dn-119763035" class="down">
<a href="javascript:voting(119763035,-1)" class="voting" data-article="119763035" id="dn-119763035" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-51</span>
</a>
</li>
<li class="comments">
<a href="/article/119763035" id="c-119763035" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119763035" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">没那么简单6j：</span>
<div class="main-text">
回复 14楼：我是湖南的，我会起义
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


7

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762112'>


<div class="author clearfix">
<a href="/users/31557645/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3155/31557645/thumb/201711171208508.JPEG?imageView2/1/w/90/h/90" alt="桃花岛的东小邪">
</a>
<a href="/users/31557645/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
桃花岛的东小邪
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/119762112" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


大学上课，高数老师要检查作业，小柳没写，但他故作淡定地对老师说，“老师，我作业放宿舍了，您不信可以问我舍友。”说着指了指小黑。<br/>小黑仰起头：“老师，他一个字都没写。”

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">7958</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762112" data-share="/article/119762112" id="c-119762112" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">69</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762112" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762112" class="up">
<a href="javascript:voting(119762112,1)" class="voting" data-article="119762112" id="up-119762112" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">8021</span>
</a>
</li>
<li id="vote-dn-119762112" class="down">
<a href="javascript:voting(119762112,-1)" class="voting" data-article="119762112" id="dn-119762112" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-63</span>
</a>
</li>
<li class="comments">
<a href="/article/119762112" id="c-119762112" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762112" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">情丶锋：</span>
<div class="main-text">
不怕神一样的对手  就怕猪一样的
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


65

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809712'>


<div class="author clearfix">
<a href="/users/32062099/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3206/32062099/thumb/20160628155848.jpg?imageView2/1/w/90/h/90" alt="找个炮台">
</a>
<a href="/users/32062099/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
找个炮台
</h2>
</a>
<div class="articleGender manIcon">34</div>
</div>

<a href="/article/118809712" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


早上坐地铁，人不是太多，顺手将香蕉放在身边的座位上，下一站上来一妹子，只顾着看手机，也没注意就坐在我的香蕉上了，我着急喊了一声，小心我的香蕉要折了，妹子吓了一跳，喊到：好疼，怎么这么硬！本来没什么，可是旁边一漂亮姐姐却捂着嘴吭吭的笑了起来！搞不明白

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">3849</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/118809712" data-share="/article/118809712" id="c-118809712" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">37</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_118809712" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809712" class="up">
<a href="javascript:voting(118809712,1)" class="voting" data-article="118809712" id="up-118809712" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">3920</span>
</a>
</li>
<li id="vote-dn-118809712" class="down">
<a href="javascript:voting(118809712,-1)" class="voting" data-article="118809712" id="dn-118809712" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-71</span>
</a>
</li>
<li class="comments">
<a href="/article/118809712" id="c-118809712" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/118809712" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">｀凡人、oO：</span>
<div class="main-text">
你的香蕉是竖着放的吗？如果不是竖着放，怎么会折？
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


20

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762342'>


<div class="author clearfix">
<a href="/users/33807867/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3380/33807867/thumb/20171120010403.JPEG?imageView2/1/w/90/h/90" alt="鲜味咸饭">
</a>
<a href="/users/33807867/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
鲜味咸饭
</h2>
</a>
<div class="articleGender manIcon">25</div>
</div>

<a href="/article/119762342" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


刚结婚时跟老婆吵架！吵的激动我摔了凳子！结果没到一分钟，老妈噔噔噔的上了楼，怕老妈怪老婆，正准备替老婆说话！老妈揪着我耳朵就开始骂了起来:你个作死的东西，来，再给我摔一个试试？？把我也摔了，来～

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2902</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762342" data-share="/article/119762342" id="c-119762342" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">47</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762342" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762342" class="up">
<a href="javascript:voting(119762342,1)" class="voting" data-article="119762342" id="up-119762342" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2939</span>
</a>
</li>
<li id="vote-dn-119762342" class="down">
<a href="javascript:voting(119762342,-1)" class="voting" data-article="119762342" id="dn-119762342" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-37</span>
</a>
</li>
<li class="comments">
<a href="/article/119762342" id="c-119762342" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119762342" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">哆啦A梦ア：</span>
<div class="main-text">
亲妈呀，知道你找个老婆不容易，万一把老婆气跑了，你就找不到老婆了
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


52

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762934'>


<div class="author clearfix">
<a href="/users/3309111/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/330/3309111/thumb/20171117063717.JPEG?imageView2/1/w/90/h/90" alt="生活枯燥乏味">
</a>
<a href="/users/3309111/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
生活枯燥乏味
</h2>
</a>
<div class="articleGender manIcon">26</div>
</div>

<a href="/article/119762934" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


大叔找小萝莉问路：“公安局怎么走？”小萝莉看了大叔两眼，问：“你是想走路去呢还是坐车去呢？”“可以坐车去？那当然是坐车了！” 于是，小萝莉把怀里的钱包递给大叔：“你把这个那好。”大叔接过钱包后，小萝莉立刻大叫：抢劫啦！十分钟后，大叔坐着公安局的押送车，华丽的离开了现场。

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">1074</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762934" data-share="/article/119762934" id="c-119762934" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">13</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762934" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762934" class="up">
<a href="javascript:voting(119762934,1)" class="voting" data-article="119762934" id="up-119762934" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">1096</span>
</a>
</li>
<li id="vote-dn-119762934" class="down">
<a href="javascript:voting(119762934,-1)" class="voting" data-article="119762934" id="dn-119762934" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-22</span>
</a>
</li>
<li class="comments">
<a href="/article/119762934" id="c-119762934" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119763245'>


<div class="author clearfix">
<a href="/users/33138205/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/3313/33138205/thumb/2016121916032218.JPEG?imageView2/1/w/90/h/90" alt="与迩同笑万古丑">
</a>
<a href="/users/33138205/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
与迩同笑万古丑
</h2>
</a>
<div class="articleGender manIcon">22</div>
</div>

<a href="/article/119763245" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


瞬间感觉我双十一的货慢一点也没关系了，哈哈哈[笑哭][笑哭][笑哭]

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/119763245" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11976/119763245/medium/app119763245.jpg" alt="糗事#119763245" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">2581</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119763245" data-share="/article/119763245" id="c-119763245" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">76</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119763245" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119763245" class="up">
<a href="javascript:voting(119763245,1)" class="voting" data-article="119763245" id="up-119763245" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">2610</span>
</a>
</li>
<li id="vote-dn-119763245" class="down">
<a href="javascript:voting(119763245,-1)" class="voting" data-article="119763245" id="dn-119763245" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-29</span>
</a>
</li>
<li class="comments">
<a href="/article/119763245" id="c-119763245" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>


<a href="/article/119763245" class="indexGodCmt" onclick="_hmt.push(['_trackEvent','web_list_comment-popular','chick'])" rel="nofollow" target="_blank">
<div class="cmtMain">
<span class="cmt-god"></span>






<span class="cmt-name">夜空中最亮的声音：</span>
<div class="main-text">
我有一个硬梆梆的想法，和一个黏糊糊的建议。还有一个湿哒哒的过程，和一个软绵绵的结局。真想抱着你的破折号，摸着你的冒号，亲抚你的句号，举着我的感叹号，穿过你的小括号，在里面留下一串省略号....
<div class="likenum">
<img src="//static.qiushibaike.com/images/newarticle/like@1.5.png?v=b7f830b3bb97b559891af61444d3b4ad">


40

</div>
</div>
</div>
</a>

</div>







<div class="article block untagged mb15 typs_hot" id='qiushi_tag_119762313'>


<div class="author clearfix">
<a href="/users/16807715/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//pic.qiushibaike.com/system/avtnew/1680/16807715/thumb/20160219231007.jpg?imageView2/1/w/90/h/90" alt="释HUa1">
</a>
<a href="/users/16807715/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
释HUa1
</h2>
</a>
<div class="articleGender manIcon">101</div>
</div>

<a href="/article/119762313" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


哈哈哈，神评！

</span>

</div>
</a>
<!-- 图片或gif -->



<div class="thumb">

<a href="/article/119762313" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/11976/119762313/medium/app119762313.jpg" alt="糗事#119762313" class="illustration" width="100%" height="auto">
</a>
</div>


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">873</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/119762313" data-share="/article/119762313" id="c-119762313" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">8</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_119762313" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-119762313" class="up">
<a href="javascript:voting(119762313,1)" class="voting" data-article="119762313" id="up-119762313" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">886</span>
</a>
</li>
<li id="vote-dn-119762313" class="down">
<a href="javascript:voting(119762313,-1)" class="voting" data-article="119762313" id="dn-119762313" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-13</span>
</a>
</li>
<li class="comments">
<a href="/article/119762313" id="c-119762313" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>







<div class="article block untagged mb15 typs_old" id='qiushi_tag_118809851'>


<div class="author clearfix">
<a href="/users/28819200/" target="_blank" rel="nofollow" style="height: 35px" onclick="_hmt.push(['_trackEvent','web-list-author-img','chick'])">

<img src="//static.qiushibaike.com/images/thumb/missing.png?imageView2/1/w/90/h/90" alt="中楠。">
</a>
<a href="/users/28819200/" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-author-text','chick'])">
<h2>
中楠。
</h2>
</a>
<div class="articleGender womenIcon">21</div>
</div>

<a href="/article/118809851" target="_blank" class="contentHerf" onclick="_hmt.push(['_trackEvent','web-list-content','chick'])">
<div class="content">
<span>


看到一个美女糗友挺好看的，就是牙不太好，我居然一直叫人家去矫正牙，虽然发小跟同村的小伙伴好多去矫正牙后都美美的，但是我一直劝人家人家会不会以为我是骗子

</span>

</div>
</a>
<!-- 图片或gif -->


<div class="stats">
<!-- 笑脸、评论数等 -->


<span class="stats-vote"><i class="number">366</i> 好笑</span>
<span class="stats-comments">
<span class="dash"> · </span>
<a href="/article/118809851" data-share="/article/118809851" id="c-118809851" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment','chick'])">
<i class="number">5</i> 评论
</a>
</span>
</div>
<div id="qiushi_counts_118809851" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-118809851" class="up">
<a href="javascript:voting(118809851,1)" class="voting" data-article="118809851" id="up-118809851" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-funny','chick'])">
<i></i>
<span class="number hidden">381</span>
</a>
</li>
<li id="vote-dn-118809851" class="down">
<a href="javascript:voting(118809851,-1)" class="voting" data-article="118809851" id="dn-118809851" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-list-cry','chick'])">
<i></i>
<span class="number hidden">-15</span>
</a>
</li>
<li class="comments">
<a href="/article/118809851" id="c-118809851" class="qiushi_comments" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-comment01','chick'])">
<i></i>
</a>
</li>
</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>





<!-- 全局翻页组件 -->

<ul class="pagination">


<li>
<span class="current" >
1
</span>
</li>




<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
</li>



<li>
<a href="/hot/page/3/" rel="nofollow">
<!--<a href="/hot/page/3/" rel="nofollow">-->
<span class="page-numbers">
3
</span>
</a>
</li>



<li>
<a href="/hot/page/4/" rel="nofollow">
<!--<a href="/hot/page/4/" rel="nofollow">-->
<span class="page-numbers">
4
</span>
</a>
</li>



<li>
<a href="/hot/page/5/" rel="nofollow">
<!--<a href="/hot/page/5/" rel="nofollow">-->
<span class="page-numbers">
5
</span>
</a>
</li>



<li>
<span class="dots">
…
</span>
</li>


<li>
<a href="/hot/page/13/" rel="nofollow">
<!--<a href="/hot/page/13/" rel="nofollow">-->
<span class="page-numbers">
13
</span>
</a>
</li>


<li>
<a href="/hot/page/2/" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="next">
下一页
</span>
</a>
</li>

</ul>


</div>



<div class="col2">
<div id="sidebar" class="sidebar">

<div class="shopwindow">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29674533"></a>');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29674533";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29674533";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- <script type="text/javascript">
var cpro_id = "u693365";
</script>
<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"></script> -->
</div>

<div class="shopwindow" id="listAd2">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- 新广告代码：2017-05-03 -->
<script type="text/javascript">
/*右侧2*/
// var cpro_id = "u693365";
// document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
// 2017-5-23 修改
// FTAPI_slotid = 1026761;FTAPI_sync = true
// document.write('<script src="//pic.fastapi.net/sdk/js/a.js" charset="utf-8"><\/script>')
</script>
</div>


<div class="sidebar-other">
<img src="/static/images/productlist/ctrl_d.png">
<p>把糗事百科加入收藏夹</p>
</div>
<div class="sidebar-hot clearfix" id="sidebar-qrcode">
<div class="float-left qrcode">
<img src="/static/images/web_v3/sidebar/qiubai_qrcode.png" alt="糗事百科 APP 下载二维码">
</div>
<div class="float-left btn-box">
<a href="javascript:void(0)" class="btn-download ios" onclick="window.open('https://itunes.apple.com/cn/app/id422853458?mt=8')" target="_blank">iOS 下载</a>
<a href="javascript:void(0)" class="btn-download android" onclick="window.open('http://static.qiushibaike.com/qiushibaike.apk')" target="_blank">Android 下载</a>
<p class="tips">扫码下载糗事百科app</p>
</div>
</div>
<div class="sidebar-hot clearfix">
<h3>爆笑糗事精选</h3>
<ul>

<li class="item">
<a href="/article/119755889" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11975/119755889/medium/app119755889.jpg?imageView2/1/w/146/h/146" alt="………………割"/></span>
</a>
<a href="/article/119755889" title="………………割" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>………………割</p>
</a>
</li>

<li class="item">
<a href="/article/119737657" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11973/119737657/medium/app119737657.jpg?imageView2/1/w/146/h/146" alt="是亲生的不"/></span>
</a>
<a href="/article/119737657" title="是亲生的不" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>是亲生的不</p>
</a>
</li>

<li class="item">
<a href="/article/119674095" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11967/119674095/medium/app119674095.jpg?imageView2/1/w/146/h/146" alt="月供再高是属于您个人资产"/></span>
</a>
<a href="/article/119674095" title="月供再高是属于您个人资产" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>月供再高是属于您个人资产</p>
</a>
</li>

<li class="item">
<a href="/article/119749017" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11974/119749017/medium/app119749017.jpg?imageView2/1/w/146/h/146" alt="凑够五个字"/></span>
</a>
<a href="/article/119749017" title="凑够五个字" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>凑够五个字</p>
</a>
</li>

<li class="item">
<a href="/article/119688081" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11968/119688081/medium/app119688081.jpg?imageView2/1/w/146/h/146" alt="把顺风车乘客送到了她的终点"/></span>
</a>
<a href="/article/119688081" title="把顺风车乘客送到了她的终点" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>把顺风车乘客送到了她的终点</p>
</a>
</li>

<li class="item">
<a href="/article/119696261" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11969/119696261/medium/app119696261.jpg?imageView2/1/w/146/h/146" alt="对着老板说凉皮是凉的还是热的"/></span>
</a>
<a href="/article/119696261" title="对着老板说凉皮是凉的还是热的" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>对着老板说凉皮是凉的还是热的</p>
</a>
</li>

<li class="item">
<a href="/article/119686167" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="//pic.qiushibaike.com/system/pictures/11968/119686167/medium/app119686167.jpg?imageView2/1/w/146/h/146" alt="余生缺个你"/></span>
</a>
<a href="/article/119686167" title="余生缺个你" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>余生缺个你</p>
</a>
</li>

<li class="item">
<a href="/article/119752549" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<span><img src="?imageView2/1/w/146/h/146" alt="希望大家都下楼拿快递别让人家等太久"/></span>
</a>
<a href="/article/119752549" title="希望大家都下楼拿快递别让人家等太久" rel="nofollow" onclick="_hmt.push(['_trackEvent','web-sidebar-jingxuan','chick'])">
<p>希望大家都下楼拿快递别让人家等太久</p>
</a>
</li>

</ul>
</div>
<div class="sidebar-hot clearfix" id="sidebar-tab">
<div class="tab-head">
<h3 class="active" data-type="0">热门</h3>
<h3 data-type="1">话题</h3>
<h3 data-type="2">专区</h3>
<h3 data-type="3">推荐</h3>
</div>
<div class="sidebar-tag-block tab-content0">


<li><i># </i><a href="/joke/2466920/">老婆你爱我吗表情包</a><i> #</i></li>

<li><i># </i><a href="/joke/2466789/">想要传个简讯给你我好想好想你</a><i> #</i></li>

<li><i># </i><a href="/joke/2464460/">画漂亮美丽的宇宙公主</a><i> #</i></li>

<li><i># </i><a href="/joke/2463866/">大班区域活动我要上小学说课稿</a><i> #</i></li>

<li><i># </i><a href="/joke/2460081/">繁星直播客服</a><i> #</i></li>

<li><i># </i><a href="/joke/2461644/">领导要我每天写工作清单</a><i> #</i></li>

<li><i># </i><a href="/joke/2461961/">不想长大,舞蹈</a><i> #</i></li>

<li><i># </i><a href="/joke/2464931/">香港我要发达演员lily</a><i> #</i></li>

<li><i># </i><a href="/joke/2463876/">大班我要上小学活动反思</a><i> #</i></li>

<li><i># </i><a href="/joke/2459638/">我要投诉洒水车</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content1 hide">


<li><i># </i><a href="/joke/2467574/">我爱家乡辽宁本溪</a><i> #</i></li>

<li><i># </i><a href="/joke/2467573/">我爱家乡的银利是因为</a><i> #</i></li>

<li><i># </i><a href="/joke/2467572/">我爱家乡一种植物</a><i> #</i></li>

<li><i># </i><a href="/joke/2467571/">我爱家乡的春天植物园</a><i> #</i></li>

<li><i># </i><a href="/joke/2467570/">我爱家乡的大山应该怎么写</a><i> #</i></li>

<li><i># </i><a href="/joke/2467569/">美丽缙云我爱家乡</a><i> #</i></li>

<li><i># </i><a href="/joke/2467568/">我爱家乡沈阳手工作品</a><i> #</i></li>

<li><i># </i><a href="/joke/2467567/">我爱家乡手工展</a><i> #</i></li>

<li><i># </i><a href="/joke/2467566/">我爱家乡的萝卜干</a><i> #</i></li>

<li><i># </i><a href="/joke/2467565/">搜我爱家乡水果</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content2 hide">


<li><i># </i><a href="/key/4682977/">广东话+动</a><i> #</i></li>

<li><i># </i><a href="/key/4683739/">就是要你说爱我阅读</a><i> #</i></li>

<li><i># </i><a href="/key/4702769/">我的好妈妈舞蹈大全</a><i> #</i></li>

<li><i># </i><a href="/key/4677850/">你说呢的英文</a><i> #</i></li>

<li><i># </i><a href="/key/4679549/">妈妈,我想对你说,周记.</a><i> #</i></li>

<li><i># </i><a href="/key/4700169/">唤醒手机用什么词语好</a><i> #</i></li>

<li><i># </i><a href="/key/4690877/">中国好声音刘欢落泪</a><i> #</i></li>

<li><i># </i><a href="/key/4681939/">静静的听出你说的爱我</a><i> #</i></li>

<li><i># </i><a href="/key/4689878/">中国好声音汪峰耿斯汉</a><i> #</i></li>

<li><i># </i><a href="/key/4689001/">中国好声音黑幕太多</a><i> #</i></li>


</div>
<div class="sidebar-tag-block tab-content3 hide">


<li><i># </i><a href="/key/4705199/">中国好舞蹈最后一轮麦秋成音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705198/">中国好舞蹈史健凯背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705197/">中国好舞蹈范文博背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705196/">中国好舞蹈第十期背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705195/">中国好舞蹈极品妖男背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705194/">中国好舞蹈李健背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705193/">中国好舞蹈张洪艺背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705192/">中国好舞蹈陈智明背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705191/">中国好舞蹈麦秋成背景音乐</a><i> #</i></li>

<li><i># </i><a href="/key/4705190/">中国好舞蹈白玛次仁背景音乐</a><i> #</i></li>


</div>
</div>

<div class="shopwindow" id="listAd3">
<!-- 55736473：web-右侧悬浮-up 类型：固定 尺寸：300x250-->
<!-- <script type="text/javascript">
document.write('<a style="display:none!important" id="tanx-a-mm_108378320_8760716_29640993"></a >');
tanx_s = document.createElement("script");
tanx_s.type = "text/javascript";
tanx_s.charset = "gbk";
tanx_s.id = "tanx-s-mm_108378320_8760716_29640993";
tanx_s.async = true;
tanx_s.src = "https://phs.tanx.com/ex?i=mm_108378320_8760716_29640993";
tanx_h = document.getElementsByTagName("head")[0];
if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script> -->
<!-- 新广告代码：2017-05-03 -->
<!-- <script>
var cpro_id = "u1101312";
document.write('<script type="text/javascript" src="https://cpro.baidustatic.com/cpro/ui/c.js"><\/script>');
</script> -->
</div>

<div class="shopwindow">
<!-- 2017.10.16 注释 -->
<!-- <script type="text/javascript" src="https://s.haiyunimg.com/SSP/30169.js"></script> -->
<!-- 2017.10.16 添加 -->
<script>
var mediav_ad_pub = 'klT513_2129270';
var mediav_ad_width = '300';
var mediav_ad_height = '250';
</script>
<script type="text/javascript" language="javascript" charset="utf-8" src="//static.mediav.com/js/mvf_g2.js"></script>
</div>

</div>
</div>



</div>
</div>


<div class="foot">

<div class="foot-nav clearfix">
<div class="foot-nav-col">
<h3>
关于
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#team" target="_blank" rel="nofollow">
关于糗百
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#tech" target="_blank" rel="nofollow">
加入我们
</a>
</li>
<li>
<a href="//about.qiushibaike.com/web_jobs.html#contact" target="_blank" rel="nofollow">
联系方式
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
帮助
</h3>
<ul>
<li>
<a href="//about.qiushibaike.com/feedback.html" target="_blank" rel="nofollow">
在线反馈
</a>
</li>
<li>
<a href="//about.qiushibaike.com/agreement.html" target="_blank" rel="nofollow">
用户协议
</a>
</li>
<li>
<a href="//about.qiushibaike.com/policy.html" target="_blank" rel="nofollow">
隐私政策
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
下载
</h3>
<ul>
<li>
<a href="http://android.myapp.com/android/appdetail.jsp?appid=107431&icfa=15144196000105020000&lmid=2031"
target="_blank" rel="external nofollow">
Android 客户端
</a>
</li>
<li>
<a href="http://itunes.apple.com/app/id422853458" target="_blank" rel="external nofollow">
iPhone 客户端
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
关注
</h3>
<ul>
<li>
<a href="#" class="foot-wechat">
微信
<div class="foot-wechat-tips">
<span class="foot-wechat-icon"></span>
手机扫描二维码关注
</div>
</a>
</li>
<li>
<a href="http://weibo.com/qiushibaike" target="_blank" rel="external nofollow">
新浪微博
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058" target="_blank" rel="external nofollow">
QQ空间
</a>
</li>
</ul>
</div>
<div class="foot-nav-col">
<h3>
组织
</h3>
<ul>
<li>
<a href="http://shang.qq.com/wpa/qunwpa?idkey=da34d190ca97a0b21d64ebc6f3ab72c076ed35820e629b78fcf9f6a78f7063cd"
target="_blank" rel="external nofollow">
网站反馈群
</a>
</li>
<li>
<a href="http://user.qzone.qq.com/1492495058/blog/1408597608" target="_blank"
rel="external nofollow">
官方粉丝群
</a>
</li>
</ul>
</div>
</div>
<div class="foot-copyrights">
<!-- <p>&copy; Qiushibaike.com 糗事百科版权所有</p>
<p>
<span>京ICP备14028348号-1</span>
<span>京ICP证140448号</span>
<span>京网文[2017]2369-247号</span>
<span>
<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a>
</span>
</p>
<p style="margin-top:8px">友际无限（北京）科技有限公司</p>
<p style="margin-top:8px">
<span>互联网违法和不良信息举报电话：010-84872896</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p> -->
<p>互联网ICP备案：京ICP备14028348号-1</p>
<p>
<span>广播电视节目制作经营许可证：（京）字第08319号</span>
<span>网络文化经营许可证：京网文[2017]2369-247号</span>
</p>
<p style="margin-top: 8px">电信与信息服务业务经营许可证：京ICP证140448号</p>
<p>
<span>计算机信息网络国际联网单位备案：<a style='color:#333' target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502031601" rel="nofollow"><img style='vertical-align: top;' src="/static/images/beian.png?v=d0289dc0a46fc5b15b3363ffa78cf6c7" />京公网安备11010502031601号</a></span>
</p>
<br>
<p style="margin-top: 8px">友际无限（北京）科技有限公司</p>
<p>
<span>违法和不良信息举报电话：010-84872896</span>
<span>邮箱：kefu@qiushibaike.com</span>
</p>
<br>
<p style="margin-top: 8px">&copy; Qiushibaike.com 糗事百科版权所有</p>
</div>
</div>


<div class="signin-box" id="login-form">
<div class="sigin-left">
<div class="signin-account clearfix">
<h4 class="social-signin-heading">社交帐号登录</h4>
<a rel="external nofollow" oauth_href href="https://open.weixin.qq.com/connect/qrconnect?appid=wx559af2d26b56c655&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession%3Fsrc%3Dwx&response_type=code&scope=snsapi_login#wechat_redirect" class="social-btn social-wechat">
使用 微信 账号</a>
<a rel="external nofollow" oauth_href href="https://api.weibo.com/oauth2/authorize?client_id=63372306&redirect_uri=http%3A%2F%2Fwww.qiushibaike.com%2Fnew4%2Fsession" class="social-btn social-weibo">
使用 微博 账号</a>
<a rel="external nofollow" oauth_href href="https://graph.qq.com/oauth2.0/authorize?which=Login&display=pc&client_id=100251437&response_type=code&redirect_uri=www.qiushibaike.com/new4/session?src=qq" class="social-btn social-qq">
使用 QQ 账号 </a>
</div>
<div class="signin-form clearfix">
<h4 class="social-signin-heading">糗事百科账号登录</h4>
<form method="post" action="/new4/session">
<input type="hidden" name="_xsrf" value="2|a26d8990|0c5a59f134dd74c4de57f7803ed9cabd|1511145325"/>
<div class="signin-section clearfix">
<input type="text" class="form-input form-input-first" name="login" placeholder="昵称或邮箱">
<input type="password" class="form-input" name="password" placeholder="密码">
<input type="checkbox" id="remember_me" name="remember_me" checked="" value="checked" style="display:none">
</div>
<div class="signin-error" id="signin-error"></div>
<button type="submit" id="form-submit" class="form-submit">登录</button>
</form>
</div>
<div class="signin-foot clearfix">
<a rel="nofollow" href="/new4/fetchpass" class="fetch-password">忘记密码?</a>
</div>
</div>
</div>

<div class="float-nav">
<a class="float-nav-backtop" href="#" rel="nofollow">
<span class="float-nav-backtop-icon"></span>
</a>
</div>

<!--[if gte IE 6]>
<script type="text/javascript" src="//static.qiushibaike.com/js/src/web/json3.js?v=3a7f66a11a09842cd7555fad039657be"></script>
<![endif]-->
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/libs.min.js?v=bc8ddd36f0e7fed7c27f437c17f23ce0"></script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/app.min.js?v=fb527abdfeb0ca7dcd7ac97d941b61f3"></script>



<script type="text/javascript">
// Google Analytics
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-8780108-1', 'auto');
ga('send', 'pageview');
</script>

<script type="text/javascript" async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script type="text/javascript" src="https://cbjs.baidu.com/js/m.js"></script>
<script type="text/javascript">



window.broadJson = '[{&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;var cpro_id = &#39;u693365&#39;;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-sidebar-01&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;https://cpro.baidustatic.com/cpro/ui/c.js&quot;, &quot;start_time&quot;: &quot;2017-08-31 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;百度联盟&quot;, &quot;end_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;id&quot;: &quot;104&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 16:32:10&quot;, &quot;channel&quot;: &quot;&quot;}, {&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;ADEZ_slotid = 1026761;ADEZ_target=&#39;web-sidebar-02&#39;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-sidebar-02&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;//pic.ggxt.net/sdk/js/core.js&quot;, &quot;start_time&quot;: &quot;2017-08-31 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;其他&quot;, &quot;end_time&quot;: &quot;2018-09-04 00:00:00&quot;, &quot;id&quot;: &quot;105&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 16:33:18&quot;, &quot;channel&quot;: &quot;&quot;}, {&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;var cpro_id = &#39;u1101312&#39;;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-sidebar-03&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;https://cpro.baidustatic.com/cpro/ui/c.js&quot;, &quot;start_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;百度联盟&quot;, &quot;end_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;id&quot;: &quot;106&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 17:16:31&quot;, &quot;channel&quot;: &quot;&quot;}, {&quot;status&quot;: &quot;3&quot;, &quot;code&quot;: &quot;&lt;script&gt;&lt;ins class=&#39;adsbygoogle&#39; style=&#39;display:inline-block;width:728px;height:90px&#39; data-ad-client=&#39;ca-pub-7443704194229694&#39; data-ad-slot=&#39;9826878184&#39;&gt;&lt;/ins&gt;&lt;/script&gt;&quot;, &quot;name&quot;: &quot;web-foot&quot;, &quot;count_id&quot;: &quot;&quot;, &quot;url&quot;: &quot;//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js&quot;, &quot;start_time&quot;: &quot;2017-08-31 00:00:00&quot;, &quot;system&quot;: &quot;notlimited&quot;, &quot;site&quot;: &quot;web&quot;, &quot;master&quot;: &quot;谷歌&quot;, &quot;end_time&quot;: &quot;2018-08-28 00:00:00&quot;, &quot;id&quot;: &quot;103&quot;, &quot;position&quot;: &quot;&quot;, &quot;created_at&quot;: &quot;2017-08-31 16:29:51&quot;, &quot;channel&quot;: &quot;&quot;}]'
</script>
<script type="text/javascript" src="//static.qiushibaike.com/js/dist/web/v3/adsAdmin.min.js?v=9c42f35ae43e17caf141e9d6ebe32cbb"></script>
</body>
</html>

>>> content = response.read().decode('utf-8')
pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]
    
>>> content = response.read().decode('utf-8')
>>> pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="st
		     
SyntaxError: EOL while scanning string literal
>>> items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]


Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 're' is not defined
>>> import urllib
>>> import urllib2
>>> import re

>>> page = 1
>>> url = 'http://www.qiushibaike.com/hot/page/' + str(page)
>>> user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
>>> headers = { 'User-Agent' : user_agent }
>>> try:
	request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?cl
			 
  File "<pyshell#30>", line 4
    response = urllib2.urlopen(request)
                                      ^
IndentationError: unindent does not match any outer indentation level
>>> request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    
>>> items = re.findall(pattern,content)

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>> items = re.findall(pattern,content)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>> items = re.findall(pattern,content)
    for item in items:
	    

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>>  items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
	
  File "<pyshell#35>", line 2
    items = re.findall(pattern,content)
    ^
IndentationError: unexpected indent
>>> items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    items = re.findall(pattern,content)
NameError: name 'pattern' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
