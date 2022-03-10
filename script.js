function renderLine(){
    Highcharts.chart('container', {

        title: {
            text: 'K Core Sentiment Analysis'
        },
    
        yAxis: {
            title: {
                text: 'Proportion of Tweets'
            }
        },
    
        xAxis: {
            accessibility: {
                rangeDescription: 'Number of degrees'
            },
            title: {
                text: 'Number of degrees'
            }
        },
    
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },
    
        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 1
            }
        },
    
        series: [{
            name: 'Positive',
            data: [0.151588259,0.141717453,0.12571512,0.124396327,0.112749862,0.114325505,0.11531926,0.105294194,0.110808704,0.102635572,
                0.103795891,0.103981371,0.112963551,0.103951464,0.105985499,0.101036227,0.095125506,0.105743045,
                0.098778134,0.098686658,0.103574866,0.10243541,0.091044939,0.099205347,0.118339134,0.106942633,
                0.107826602,0.112951845,0.10944659,0.111752404,0.108148924,0.096294005,0.125061962,0.123875305,
                0.099164811,0.111020959,0.101460386,0.101792217,0.109582197,0.127850986,0.120274463,0.086337982,
                0.108060036,0.107381691,0.085603763,0.118241144,0.121997597,0.113026475,0.115162056,0.077457715,
                0.130982955,0.125935014,0.06692682,0.110672864, 0.122565188, 0.099824627, 0.128106592, 0.097092452, 0.10423602, 0.108869786]
        }, {
            name: 'Negative',
            data: [0.234310133,0.243376848,0.247742952,0.248113881,0.257359251,0.257581446,0.255890498,0.260089132,
                0.268380496,0.262417086,0.261228987,0.269658894,0.272745382,0.272635392,0.266020674,0.27683467,
                0.272802361,0.296945002,0.273153789,0.271938327,0.268738354,0.271488948,0.259360747,0.253278186,
                0.285684306,0.304235658,0.329690924,0.272687915,0.347662569,0.374334221,0.395592517,0.39063719,
                0.402185742,0.364995685,0.375998171,0.389306682,0.382088368,0.26495424,0.382323379,0.384584991,
                0.361966172,0.40166593,0.409836832,0.400584057,0.449540081,0.393291366,0.37414605,0.409077384,
                0.403120649,0.475363522,0.428126128,0.438199018,0.443003877,0.465469333,0.424153993,0.466429555,
                0.414336278,0.433568873,0.387438578,0.389112292]
        }, {
            name: 'Neutral',
            data: [0.61380938,0.614685741,0.62639545,0.627271021,0.629890887,0.628093047,0.627943862,0.634616675,
                0.620267616,0.634947343,0.634298988,0.626359736,0.614291068,0.623413142,0.627993826,0.622129106,
                0.63207213,0.597311952,0.628068076,0.629375017,0.627686783,0.62607564,0.649594313,0.646079686,
                0.595976558,0.588821706,0.56248248,0.614360241,0.542890837,0.513913378,0.496258559,0.5130688,
                0.472752304,0.511129016,0.52483702,0.499672358,0.516451253,0.633253543,0.508094422,0.48756402,
                0.517759379,0.51199608,0.482103134,0.492034253,0.464856145,0.488467491,0.503856358,0.477896144,
                0.481717293,0.447178762,0.440890908,0.435865957,0.490069303,0.423857797,0.45328081,0.433745826,
                0.457557127,0.469338682,0.508325396,0.502017919]
        }],
    
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }
    
    });
}

function renderBot(){
    Highcharts.chart('bot', {

        title: {
            text: 'K Core Bot User Detection'
        },
    
        yAxis: {
            title: {
                text: 'Proportion of Bot Users'
            }
        },
    
        xAxis: {
            accessibility: {
                rangeDescription: 'Number of degrees'
            },
            title: {
                text: 'Number of degrees'
            }
        },
    
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },
    
        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 1
            }
        },
    
        series: [{
            name: 'Percentage of Bot User',
            data: [0.392677473,0.157574424,0.164960515,0.142607174,0.157209033,0.181785586,0.168163265,0.153736991,0.294117647,
                   0.139300533,0.18818514,0.140978817,0.207341944,0.23782235,0.118985127,0.225287356,0.128514056,0.171240395,
                   0.113365155,0.124871001,0.169014085,0.138601036,0.255319149,0.170035672,0.135664336,0.269117647,0.249607535,
                   0.125156446,0.088036117,0.130584192,0.114441417,0.092150171,0.116504854,0.145205479,0.125423729,0.128205128,
                   0.072327044,0.073921971,0.164893617,0.15625,0.234042553,0.176470588,0.221276596,0.249480249,0.391752577,0.113970588,
                   0.303571429,0.203296703,0.258333333,0.214876033,0.133858268,0.240740741,0.117533719,0.3515625,0.252525253,
                   0.223684211,0.214285714,0.289962825,0.215517241,0.181113801]
        }],
    
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }
    
    });
}


function renderAuthor(){
    Highcharts.chart('author', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Number of Tweets Per User'
        },
        xAxis: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 1
            }
        },
        yAxis: {
          min: 0,
          title: {
            text: ''
          }
        },
        tooltip: {
          headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
          pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
          footerFormat: '</table>',
          shared: true,
          useHTML: true
        },
        plotOptions: {
          column: {
            pointPadding: 0,
            borderWidth: 0,
            groupPadding: 0,
            shadow: false
          }
        },
        series: [{
          name: 'Count',
          data: [14759476, 1597415, 442619, 174868,84570,45397,26545,16718,11031,7604,5358,3882,3072,2289,1661,1366,
            1111,933,702,493,439,428,333,257,132,97,81,50]
      
        }]
      });
      
}

function renderkcore(){
    Highcharts.chart('kcore', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Number of Nodes in K Core Decomposition'
        },
        xAxis: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 1
            }
        },
        yAxis: {
          min: 0,
          title: {
            text: ''
          }
        },
        tooltip: {
          headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
          pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
          footerFormat: '</table>',
          shared: true,
          useHTML: true
        },
        plotOptions: {
          column: {
            pointPadding: 0,
            borderWidth: 0,
            groupPadding: 0,
            shadow: false
          }
        },
        series: [{
          name: 'Count',
          data: [50037,4487719,1032701,443798,244379,153693,104749,74912,57019,43967,35298,28742,23664,
            20030,16842,14658,12231,10658,9744,8166,7448,6280,6150,5348,4144,3309,2993,3162,2436,
            1991,2016,1614,1844,1575,1163,1420,1163,1476,743,838,633,719,733,987,404,653,460,446,
            331,330,271,293,315,295,328,186,305,510,194,1437]
      
        }]
      });
      
}

function renderkPoint(){
    Highcharts.chart('point', {
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: 'AB Testing Result with K Core Decomposition with K value of 1 and 60'
        },
        xAxis: {
            title: {
                enabled: true,
                text: 'Number of Degree'
            },
            startOnTick: true,
            endOnTick: true,
            showLastLabel: true
        },
        yAxis: {
            title: {
                text: 'Z Score'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 100,
            y: 70,
            floating: true,
            backgroundColor: Highcharts.defaultOptions.chart.backgroundColor,
            borderWidth: 1
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{series.name}</b><br>',
                    pointFormat: '{point.x}, {point.y}'
                }
            }
        },
        series: [{
            name: 'Z Score',
            color: 'rgba(223, 83, 83, .5)',
            data: [[1, 13.17027264], [2, 13.06118], [3, 12.4242], [4, 12.16425], [5, 11.12431],
                [6, 10.92886], [7, 10.91911], [8, 10.34947], [9, 9.05596], [10, 9.869833],
                [11, 9.883868], [12, 9.042857], [13, 8.733289], [14, 8.603775], [15, 8.99545],
                [16, 8.097733], [17, 8.114657], [18, 6.244175], [19, 7.978793], [20, 8.079127],
                [21, 8.178614], [22, 7.75567], [23, 8.918255], [24, 9.234567], [25, 6.391091],
                [26, 4.906699], [27, 3.29684], [28, 7.425201], [29, 2.183749], [30, 0.67559],
                [31, -0.32283], [32, -0.07009], [33, -0.62346], [34, 1.151486], [35, 0.543772],
                [36, -0.00884], [37, 0.294001], [38, 7.11802], [39, 0.230863], [40, 0.181553],
                [41, 1.009405], [42, -0.46915], [43, -0.8725], [44, -0.57958], [45, -1.80776],
                [46, -0.1545], [47, 0.488799], [48, -0.64195], [49, -0.44106], [50, -2.40785],
                [51, -1.08676], [52, -1.37008], [53, -1.81634], [54, -2.25652], [55, -0.92254],
                [56, -1.7171], [57, -0.72131], [58, -1.82209], [59, -.048051], [60, 0],
                ]
    
        }]
    });
    
}

window.onload = function generateEntries(){
    renderLine();
    renderBot();
    renderAuthor();
    renderkcore();
    renderkPoint();
}





