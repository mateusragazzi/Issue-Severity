function sendSearch() {
  jQuery('#searchFormBtn').click();
}

window.addEventListener('load', () => {
  // WORD CLOUD PLUGIN
  // am4core.ready(function() {
  //   am4core.useTheme(am4themes_animated);
    
  //   var chart = am4core.create("word-clouds", am4plugins_wordCloud.WordCloud);
  //   var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

  //   series.data = words;     
  //   series.rotationThreshold = 0.7;
  //   series.dataFields.word = "tag";
  //   series.dataFields.value = "weight"; 
  //   series.labels.template.tooltipText = "{word}: {value}";
  //   // series.fontFamily = "Courier New";
  //   series.maxFontSize = am4core.percent(70);
  //   series.minFontSize = am4core.percent(8);
    
  //   $('#id-50-title').parent('g').remove();
  // });
})