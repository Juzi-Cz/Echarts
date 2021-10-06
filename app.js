//引入express模块
const express = require("express");
//创建web服务器
const app = express();
//引入path模块
const path = require("path");
//配置静态资源访问
app.use(express.static(path.join(__dirname, "public")));

//运行爬虫文件

setInterval(() => {
    console.log("数据正在爬取中....")
    const nodeCmd = require('node-cmd');
    nodeCmd.get('python', function(err, data, stderr) {
            console.log(data);
        })
        // nodeCmd.run('python getWikiList.py');
    nodeCmd.run('python getTimelineService1.py');
    // nodeCmd.run('python getStatisticsService.py');
    // nodeCmd.run('python getListByCountryTypeService2true.py');
    // nodeCmd.run('python getIndexRecommendList2.py');
    // nodeCmd.run('python getAreaStat.py');
    // nodeCmd.run('python fetchWHOArticle.py');
    // nodeCmd.run('python fetchRecentStatV2.py');
    nodeCmd.run('python fetchRecentStat.py');
    // nodeCmd.run('python fetchGoodsGuide.py');
    console.log("更新结束...");
}, 1000 * 20);
// 侦听端口
app.listen(3000, () => {
    console.log("....服务器启动成功!....");
})