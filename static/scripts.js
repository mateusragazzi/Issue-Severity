function sendSearch() {
  let issue = jQuery("#search").val();
  window.localStorage.setItem("persistFeedback", JSON.stringify({ feedback: null, issue, severityChoosed: null }));

  jQuery('#searchFormBtn').click();
}

function clearSearch() {
  jQuery("#search").val("");
  jQuery(".result").hide(200);
}

function sendFeedback(userFeedback) {
  let feedback = JSON.parse(window.localStorage.getItem("persistFeedback"));
  let severity = jQuery(".result h1").text().split(": ")[1];
  feedback.severity = severity;
  feedback.feedback = userFeedback;

  window.localStorage.setItem("persistFeedback", JSON.stringify(feedback));

  if (userFeedback) 
    persistFeedback(feedback);
  else
    askForSuggestion();
}

function askForSuggestion() {
  jQuery(".agree-or-not").hide(300);
  jQuery(".suggestion").show(500);
}

function sendChoosedSeverity() {
  let issue = jQuery("#choosed-severity option:selected").val();
  let feedback = JSON.parse(window.localStorage.getItem("persistFeedback"));
  feedback.severityChoosed = issue;

  window.localStorage.setItem("persistFeedback", JSON.stringify(feedback));
  persistFeedback(feedback);
}

function persistFeedback(feedback) {
  console.log(feedback);

  jQuery.ajax({
    url: '/save-query',
    method: 'POST',
    data: feedback,
    dataType: 'json',
    success: (response) => {
      console.log(response)
    },
    error: () => {

    }
  });

  window.localStorage.clear("persistFeedback");
  clearSearch();
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

  jQuery("#search").on('keydown', function(e) {
    if (e.keyCode === 13) {
      e.preventDefault();
      e.stopImmediatePropagation();
      sendSearch();
    }
  });

  tippy('.help #issue', {
    content: "Record and monitor suggestions and changes around the software. <br><br> <small>Leon, A. <i>Software configuration management handbook</i>, Artech House, 2015.</small>",
    theme: 'issue-severity',
    trigger: 'click',
    allowHTML: true
  });

  tippy('.help #severity', {
    content: "Reporting level, which can be: <br> <ul> <li> <b>Blocker:</b> blocks development, testing or use of software </li> <li> <b>Critical:</b> cause crash, loss of data or memory leak </li> <li> <b>Major:</b> major loss of functionality </li> <li> <b>Normal:</b> loss of functionality under certain circumstances </li> <li> <b>Minor:</b> minor loss of functionality which is easy for user to workaround </li> <li> <b>Enhancement:</b> cosmetic problem, misspelled word or others improvements </li> </ul> <small>Gomes, L., Torres, R., Côrtes, M., <i>Bug Report Severity Level Prediction in Open Source Software: A Survey and Research Opportunities</i>, 2019.</small>",
    theme: 'issue-severity',
    trigger: 'click',
    allowHTML: true
  });
})