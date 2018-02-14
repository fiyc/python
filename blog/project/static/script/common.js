function SetTimeThread(d, t){
	setTime(d, t);
	window.setInterval(function(){
		setTime(d, t);
	}, 1000);

}

function setTime(d,t){
	var time = new Date();
	var year = time.getFullYear().toString();
	var month = (time.getMonth() + 1).toString();
	var date = time.getDate().toString();
	var hour = time.getHours().toString();
	var min = time.getMinutes().toString();
	var sec = time.getSeconds().toString();
	var day = time.getDay().toString();
	if(month.length == 1)
		month = "0"+month;
	if(date.length == 1)
		date = "0"+date;
	if(hour.length == 1)
		hour = "0"+hour;
	if(min.length == 1)
		min = "0"+min;
	if(sec.length == 1)
		sec = "0"+sec;
	var dayTime = year + "年" + month + "月" + date + "日";
	var hourTime = hour + ":" + min;
	$("#" + d).html(dayTime);
	$("#" + t).html(hourTime);
}


function checkType(item){
	var list = $(item).parent().parent().find("a");
	for(var i=0; i< list.length; i++){
		$(list[i]).attr("class", "nocheck")
	}
	$(item).attr("class", "hascheck");
	$("#currentPageIndex").val(1);
	// var data = {
	// 	"typeId": $(item).attr("typeid")
	// }
	// var url = "/blogansy/" + $(item).attr("typeid")
	// $.ajax({
	// 	url:url,
	// 	success:function(data){
	// 		data = JSON.parse(data);
	// 		var dataHtml = "";
	// 		if(data != null){
	// 			for(var i=0; i<data.length; i++){
	// 				dataHtml += '<div class="chapter"><p class="time">' + data[i].TimeDesc + '</p>';
	// 				dataHtml += '<a class="chapterName" href="/detail/'+ data[i].ArticleId +'">' + data[i].Title + '</a>';
	// 				dataHtml += '<p class="readNum">阅读' + data[i].ReadNum + '</p></div>'
	// 			}
	// 		}
	// 		$(".rightPannel").html(dataHtml);

	// 	}
	// });

	var keyword = $("#keyword").val();
	var typeId = $(item).attr("typeid")
	search(typeId, keyword, 1, false);
}

function searchArticleAnsy(typeId, keyword, pageIndex){
	var url = "/ansysearch?" + "typeId=" + typeId + "&keyword=" + keyword + "&pageIndex=" + pageIndex
	var result;
	$.ajax({
		url:url,
		async: false,
		success:function(data){
			result = JSON.parse(data);
		}
	});
	return result;
}

function pushData(isAppend, data){
	$("#totalPageNum").val(data.TotalPageNum);
	var dataHtml = "";
	if( data != null){
		for(var i=0; i<data.ArticleList.length; i++){
			dataHtml += '<div class="chapter"><p class="time">' + data.ArticleList[i].TimeDesc + '</p>';
			dataHtml += '<a class="chapterName" href="/detail/'+ data.ArticleList[i].ArticleId +'">' + data.ArticleList[i].Title + '</a>';
			dataHtml += '<p class="readNum">阅读' + data.ArticleList[i].ReadNum + '</p></div>'
		}
	}

	if(isAppend){
		$(".rightPannel").append(dataHtml);
	}else{
		$(".rightPannel").html(dataHtml);
	}

	var pageInfoHtml = "";
	$("#pageInfo").remove();

	if (data.PageIndex >= Number($("#totalPageNum").val())){
		pageInfoHtml = '<div id="pageInfo" style="text-align:center"><span>已显示全部</span></div>';
	}else{
		pageInfoHtml = '<div id="pageInfo" style="text-align:center"><a href="javascript:void(0)" onclick="GoNextPage()">显示更多</a></div>'
	}

	$(".rightPannel").append(pageInfoHtml);


}

function search(typeId, keyword, pageIndex, isAppend){
	data = searchArticleAnsy(typeId, keyword, pageIndex);
	pushData(isAppend, data);
	if(data != null)
		return true;
	else
		return false;
}

