// This file is subject to the terms and conditions defined in
// file 'LICENSE', which is part of this source code package.
//       Copyright (c) 2009 SKR Farms (P) LTD.

var z_hctheme = 'default';
var z_hccolors = [ '#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5',
                   '#64E572', '#FF9655', '#FFF263', '#6AF9C4' ]

function hc_setoption( charttheme ) {
    var theme = charttheme ? charttheme : z_hctheme;
    hcthemes[theme] = jQuery.extend(
                            true, null,
                            hcthemes[theme],
                            { credits: { enabled: false } }
                      );
    Highcharts.setOptions( hcthemes[theme] );
}

/*************************** Tag Charts ******************************/

function chart1_tagchart( data, id ) {
    var total = 0
    dojo.forEach( data, function(item) { total += item[1]; } )

    hc_setoption( 'minimal' );
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
        },
        title: { text: '' },
        legend: {
            layout: 'vertical',
            verticalAlign: 'bottom',
            align: 'right',
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            pie: {
                size: "120%",
                center: ["30%", "50%"],
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        if (this.y > 5) return this.point.name;
                    },
                    color: 'white',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.point.name +'</b>: '
                       + Math.round((this.y/total)*100) + ' % ';
            }
        },
        series: [{
            name: 'Count',
            data: data
        }]
    });
    return chart
}

/*************************** Attachment Charts ******************************/

function chart2_user_vs_attach( data, id ) {
    var users   = dojo.map( data, "return item[0]" );
    var files   = dojo.map( data, "return item[1]" );
    var payload = dojo.map( data, "return item[2]" );

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            zoomType: 'x',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        subtitle: { text: '' },
        xAxis: [{
            maxZoom: 10,
            tickInterval: 1,
            endOnTick: true,
            startOnTick: true,
            labels: {
                rotation: -45,
                align: 'right',
                formatter: function() {
                             return (this.value >= 0) && (this.value < users.length) ?
                                    users[this.value] : '';
                           }
            }
        }],
        yAxis: [{ // Primary yAxis
            title: {
                text: 'Uploaded Payload',
                style: { color: '#89A54E' },
                margin: 100
            },
            labels: {
                formatter: function() {
                    return Math.round(this.value / 1024) + ' KB';
                },
                style: { color: '#89A54E' }
            }
        }, { // Secondary yAxis
            title: {
                text: 'Uploaded files',
                style: { color: '#4572A7' },
                margin: 60
            },
            labels: {
                style: { color: '#4572A7' }
            },
            opposite: true
        }],
        tooltip: {
            formatter: function() {
                return '<b>'+ data[this.x][0] +'</b><br/>' +
                       (this.series.name == 'files' ? 'files : ' : 'payload : ') +
                       this.y;
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        series: [{
            name: 'payload',
            color: '#89A54E',
            type: 'column',
            data: payload
        
        }, {
            name: 'files',
            color: '#4572A7',
            type: 'spline',
            yAxis: 1,
            data: files
        }]
    });
    return chart
}

function chart3_attach_vs_download( data, id ) {
    var counts  = dojo.map( data, "return item[2]" );

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'line',
            zoomType: 'x'
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            title: {
                enabled: true,
                text: 'Attachments'
            },
            maxZoom: 10
        },
        yAxis: {
            title: { text: 'Download count' },
        },
        tooltip: {
            formatter: function() {
                    return '<b>'+ data[this.x][1] + '</b>,'+ this.y;
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            line: {
                marker: {
                    enabled: true,
                    radius: 1,
                    states: {
                        hover: { enabled: true, radius: 3 }
                    }
                },
                fillOpacity: 0.1,
                lineWidth: 1,
            }
        },
        series: [{
            name: 'files',
            data: counts,
        }]
    });
    return chart
}

function chart4_attach_vs_tags( data, id ) {
    var attach_no = dojo.map( data, "return item[1].length" );
    var tagnames  = dojo.map( data, "return item[0]" );
    var filenames = function( attachs ) {
                        return dojo.map( attachs, "return item[1]" );
                    }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'column',
            zoomType: 'x'
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            title: { text: 'Tagname', margin: 80 },
            tickInterval: 1,
            labels: {
                formatter: function() { return tagnames[this.value] },
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { text: 'No. of Attachments' }
        },
        tooltip: {
            formatter: function() {
                    return '<b>'+ data[this.x][0] + '</b><br/>' +
                           filenames( data[this.x][1] ).join( '<br/>' )
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            column: {
                dataLabels: {
                    formatter: function() { return this.y },
                    enabled : true,
                    style: {
                        color: '#FFFFFF'
                    }
                }
            }
        },
        series: [{
            name: 'tagged attachments',
            data: attach_no
        }]
    });
    return chart
}


function chart5_attach_vs_time( fromdate, data, id ) {
    var count = dojo.map( data, "return item.length" )
    var files = function( items ) {
                    return items ?
                                dojo.map( items, "return '<b>'+item[1]+'</b>' + ', ' + item[2]" )
                                : ''
                }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            zoomType: 'x'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            type: 'datetime',
            maxZoom: 20 * 24 * 3600000, // Twenty days
            title: { text: null }
        },
        yAxis: {
            title: { text: 'Upload activity' },
            startOnTick: false,
            showFirstLabel: false
        },
    
        tooltip: {
            formatter: function() {
                var offset = (this.x-fromdate) / 3600 / 1000 / 24
                return files( data[offset] ).join( '<br/>' );
            }
        },
        legend: { enabled: false },
        plotOptions: {
            areaspline: {
                fillOpacity: 0.5,
                lineWidth: 1,
                marker: {
                    enabled: true,
                    radius: 1,
                    states: {
                        hover: { enabled: true, radius: 3 }
                    }
                },
                shadow: false,
                states: {
                    hover: { lineWidth: 1 }
                }
            }
        },
        series: [{
            type: 'areaspline',
            name: 'uploadedtime',
            pointInterval: 24 * 3600 * 1000,
            pointStart: fromdate,
            data: count
        }]
    });
    return chart
}

/*************************** License Charts ******************************/

function chart6_license_projects( data, id ) {
    var piedata = dojo.map( data, "return [ item[1], item[2].length ]" );
    var lic_tot = 0
    dojo.forEach( data, function(item) { lic_tot += item[2].length; } )

    hc_setoption( 'minimal' );
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
        },
        title: { text: '' },
        plotArea: {
            shadow: null,
            borderWidth: null,
            backgroundColor: null
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.point.name +'</b>: '
                       + Math.round((this.y/lic_tot)*100) +' % <br/> '
                       + data[this.point.x][2].join( '<br/>' )
            }
        },
        plotOptions: {
            pie: {
                size: "90%",
                center: ["20%", "40%"],
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    color: 'white',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        legend: {
            layout: 'vertical',
            verticalAlign: 'bottom',
            align: 'right',
            itemStyle: { fontSize : 'small' }
        },
        series: [{
            type: 'pie',
            name: 'LicenseProject',
            data: piedata,
        }]
    });
    return chart;
}


function chart7_license_vs_tags( data, id ) {
    var lic_no    = dojo.map( data, "return item[1].length" );
    var tagnames  = dojo.map( data, "return item[0]" );
    var filenames = function( fortag ) {
                        return dojo.map( fortag[1], "return item[1]" )
                    }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'column',
            zoomType: 'x',
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            title: { text: 'Tagname', margin: 80 },
            tickInterval: 1,
            labels: {
                formatter: function() { return tagnames[this.value] },
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { text: 'No. of License' }
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ data[this.x][0] + '</b><br/>' +
                       filenames( data[this.x] ).join( ', ' )
            }
        },
        plotOptions: {
            line: {
                marker: {
                    enabled: false
                },
                fillOpacity: 0.1,
                lineWidth: 1,
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        series: [{
            name: 'tagged license',
            data: lic_no
        }]
    });
    return chart
}

/*************************** Users Charts ******************************/

function chart8_users_activity( data, id ) {
    var users   = dojo.map( data, 'return item[1]' );
    var weights = dojo.map( data, 'return item[2]' );

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'column',
            zoomType: 'x',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            categories: users,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            min: 0,
            title: { 
                text: 'Total activity count',
                margin: 60
            }
        },
        plotOptions: {
            column: {
                dataLabels: {
                    formatter: function() { return this.y },
                    enabled : true,
                }
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.x +'</b><br/>'+ 'Made '+ this.y + ' updates';
            }
        },
        series: [{
            name: 'Activity',
            data: weights,
        }]
    });
    return chart;
}

function chart9_users_siteperm( data, id ) {
    var users       = dojo.map( data, 'return item[1]' );
    var siteperms   = dojo.map( data, 'return item[2].length' );
    var x_siteperms = dojo.map( data, 'return item[3].length' );
    var usersiteperms = function( username ) {
                            var u = null;
                            for(i = 0; i < data.length; i++ ) {
                                u = data[i];
                                if( u[1] == username ) { break; }
                            }
                            return u;
                        }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'column',
            zoomType: 'x',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        xAxis: {
            categories: users,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            }
        },
        yAxis: {
            min: 0,
            title: { text: 'Site Permissions' }
        },
        tooltip: {
            formatter: function() {
                var u = usersiteperms( this.x );
                return '<b>' + this.x + '</b><br/>' +
                       (this.series.name == 'granted permissions'
                            ? u[2].join( ', ' ) : u[3].join( ', ' ) )
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled : true,
                    color: '#000'
                }
            }
        },
        series: [{
                name: 'granted permissions',
                data: siteperms
            }, {
                name: 'permissions not granted',
                data: x_siteperms
        }]
    });
    return chart;
}

function chart10_project_admins( data, id ) {
    var piedata = dojo.map( data, "return [ item[1], item[2].length ]" );
    var total   = 0
    dojo.forEach( data, function(item) { total += item[2].length; } )

    hc_setoption( 'minimal' );
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
        },
        title: { text: '' },
        legend: {
            layout: 'vertical',
            verticalAlign: 'bottom',
            align: 'right',
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            pie: {
                size: "120%",
                center: ["30%", "50%"],
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    color: 'white',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.point.name +'</b> : '
                       + Math.round((this.y/total)*100) + ' % ' + '<br/>'
                       + data[this.point.x][2].join( '<br/>' )

            }
        },
        series: [{
            name: 'Project',
            data: piedata
        }]
    });
    return chart;
}

function chart11_component_owners( total, data, id ) {
    var piedata = dojo.map( data, "return [ item[1], item[2].length ]" );

    hc_setoption( 'minimal' );
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
        },
        title: { text: '' },
        legend: {
            layout: 'vertical',
            verticalAlign: 'bottom',
            align: 'right',
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            pie: {
                size: "120%",
                center: ["30%", "50%"],
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    color: 'white',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.point.name +'</b>: '
                       + Math.round((this.y/total)*100) + ' % ' + '<br/>'
                       + data[this.point.x][2].join( '<br/>' )
            }
        },
        series: [{
            name: 'Components',
            data: piedata
        }]
    });
    return chart;
}

/*************************** User Charts ******************************/

function chart12_userproject_activity( data, id ) {
    var piedata = data[2];
    var total   = 0;
    for(i = 0; i < data[2].length; i++ ) {
        total += data[2][i][1];
    }

    hc_setoption( 'minimal' );
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
        },
        title: { text: '' },
        legend: {
            layout: 'vertical',
            verticalAlign: 'bottom',
            align: 'right',
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            pie: {
                size: "120%",
                center: ["30%", "50%"],
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    color: 'white',
                    formatter: function() {
                        return piedata[this.point.x][1];
                    },
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function( _piedata ) {
                            return '<b>'+ this.point.name +'</b>: '
                                   + Math.round((this.y/total)*100) + ' % ' + '<br/>'
                                   + piedata[this.point.x][1]
            },
        },
        series: [{
            name: 'Project Activities',
            data: piedata
        }]
    });
    return chart;
}

/*************************** Milestone Charts ******************************/

function chart13_milestone_tickets( data, id ) {
    var types      = data[1];
    var severities = data[2];
    var statuses   = data[3];
    var owners     = data[4];

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            margin: [ 0, 0, 0, 80]
        },
        title: {
            text: '',
            style: {
                margin: '0 0 0 0'
            }
        },
        xAxis: {
        },
        tooltip: {
            formatter: function() {
                return '<b>' + this.point.name + ', </b>'
                       + this.point.y
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            pie: {
                dataLabels: {
                    enabled: true,
                    color: 'white',
                    formatter: function() { return this.point.y; },
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        labels: {
            items: [{
                html: 'Ticket type',
                style: {
                    left: '0px',
                    top: '30px',
                    color: 'gray'				
                }
            }, {
                html: 'Ticket severity',
                style: {
                    left: '120px',
                    top: '30px',
                    color: 'gray'				
                }
            }, {
                html: 'Ticket status',
                style: {
                    left: '250px',
                    top: '30px',
                    color: 'gray'				
                }
            }, {
                html: 'Ticket owner',
                style: {
                    left: '400px',
                    top: '30px',
                    color: 'gray'				
                }
            }]
        },
        series: [{
            type: 'pie',
            name: 'bytype',
            data: types,
            center: [20, 130],
            size: 130,
            showInLegend: false
        }, {
            type: 'pie',
            name: 'byseverity',
            data: severities,
            center: [160, 130],
            size: 130,
            showInLegend: false
        }, {
            type: 'pie',
            name: 'bystatus',
            data: statuses,
            center: [300, 130],
            size: 130,
            showInLegend: false
        }, {
            type: 'pie',
            name: 'byowners',
            data: owners,
            center: [440, 130],
            size: 130,
            showInLegend: false
        }]
    });
    return chart;
}

/*************************** Project Charts ******************************/

function chart14_project_activity( data, id ) {
    var total = 0
    dojo.forEach( data, function(item) { total += item[1]; } )

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
        },
        title: { text: '' },
        legend: {
            layout: 'vertical',
            style: {
                left: '50px',
                bottom: 'auto',
                right: 'auto',
                top: '100px'
            }
        },
        plotOptions: {
            pie: {
                size: "120%",
                center: ["30%", "50%"],
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        if (this.y > 1) return this.point.name;
                    },
                    color: 'white',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        legend: {
            layout: 'vertical',
            verticalAlign: 'bottom',
            align: 'right',
            itemStyle: { fontSize : 'small' }
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.point.name +'</b>: '
                       + Math.round((this.y/total)*100) + ' % <br/> '
                       + this.y
            }
        },
        series: [{
            name: 'Activity',
            data: data
        }]
    });
    return chart
}

function chart15_roadmap( fromdate, data, id ) {
    var mstnnames = dojo.map( data, "return item[0]" )
    var prefix    = dojo.map( data, "return item[1]" )
    var open      = dojo.map( data, "return item[2]" )
    var cancelled = dojo.map( data, "return item[3]" )
    var completed = dojo.map( data, "return item[4]" )

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'bar',
            margin: [50, 50, 100, 100]
        },
        title: {
            text: ''
        },
        xAxis: {
            gridLineWidth: 1,
            categories: mstnnames
        },
        yAxis: {
            gridLineWidth: 1,
            title: { text: 'Time', margin: 80 },
            labels: {
                rotation: -45,
                align: 'right',
                formatter: function() {
                    var thisms = fromdate + this.value * (24*3600000);
                    return Highcharts.dateFormat( "%e. %b %y", thisms );
                },
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        tooltip: {
            formatter: function() { return this.y + ' days'; }
        },
        plotOptions: {
            bar: {
                shadow: false,
            },
            series: {
                stacking: 'normal'
            }
        },
        series: [{
            name: 'completed',
            color: '#b7d9ba',
            data: completed,
        }, {
            name: 'cancelled',
            color: '#eb9898',
            data: cancelled
        }, {
            name: 'open',
            color: '#968ff5',
            data: open
        }, {
            name: 'prefix',
            color: '#FFFFFF',
            data: prefix
        }]
    });
    return chart
}

/*************************** Wiki Charts ******************************/

function chart16_wiki_cmtsvers( data, id ) {
    var wikipages = dojo.map( data, 'return item[0]' );
    var versions  = dojo.map( data, 'return item[1]' );
    var comments  = dojo.map( data, 'return item[2]' );

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'column',
            zoomType: 'x',
            margin: [ 50, 50, 120, 80]
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            categories: wikipages,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { 
                text: 'Count',
                margin: 60
            }
        },
        plotOptions: {
            column: {
                dataLabels: {
                    formatter: function() { return this.y },
                    enabled : true,
                    style: {
                        color: '#FFFFFF'
                    }
                }
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        tooltip: {
            formatter: function() {
                return this.series.name == 'Edits' ?
                            this.y + ' edits for, <br/>' + this.x :
                            this.y + ' comments for,<br/>' + this.x
            }
        },
        series: [{
            name: 'Edits',
            data: versions
        }, {
            name: 'Comments',
            data: comments
        }]
    });
    return chart;
}

function chart17_wikivotes( data, id ) {
    var wikipages = dojo.map( data, 'return item[0]' );
    var upvotes   = dojo.map( data, 'return item[1]' );
    var downvotes = dojo.map( data, 'return item[2]' );
    var totalupvotes = 0
    var totaldownvotes = 0
    dojo.forEach( data, function(x) {
                            totalupvotes += x[1];
                            totaldownvotes += x[2];
                        }
                )

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            zoomType: 'x',
            margin: [ 50, 50, 120, 80]
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            categories: wikipages,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                },
                
            },
            maxZoom: 10
        },
        yAxis: {
            title: { 
                text: 'Count',
            }
        },
        tooltip: {
            formatter: function() {
                var s;
                if (this.point.name) { // the pie chart
                    s = 'Total ' + this.point.name + ' : ' + this.y;
                } else {
                    s = this.y + ' ' + this.series.name;
                }
                return s;
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    formatter: function() { return this.y },
                    enabled : true,
                }
            }
        },
        series: [{
            type: 'column',
            name: 'Upvotes',
            data: upvotes,
            color: '#89A54E'
        }, {
            type: 'column',
            name: 'Downvotes',
            data: downvotes,
            color: '#AA4643'
        }, {
            type: 'pie',
            name: 'Total upvotes and downvotes',
            data: [{
                name: 'Upvotes',
                y: totalupvotes,
                color: '#89A54E'
            }, {
                name: 'Downvotes',
                y: totaldownvotes,
                color: '#AA4643'
            }],
            center: ['80%', '5%'],
            size: 80,
            align: 'right',
            showInLegend: false
        }]
    });
    return chart;
}

function chart18_wikiauthors( data, id ) {
    function makedata( authors, i ) {
        var data  = [];
        var total = 0;
        for(j = 0; j < authors.length; j++) {
            data[data.length] = authors[j][i][1];
            total += authors[j][i][1]; 
        }
        return [ data, total ]
    }
    function makechart( authors ) {
        var wseries = [];
        var utotal  = [];
        for(i = 0; i < authors[0].length; i++ ) {
            var username = authors[0][i][0];
            var values   = makedata( authors, i );
            wseries[wseries.length] = {
                    type : 'column',
                    name : username,
                    data : values[0]
            }
            utotal[utotal.length] = {
                    name : username,
                    y    : values[1]
            }
        }
        return [ wseries, utotal ]
    }

    var wikipages = dojo.map( data, 'return item[0]' );
    var authors   = dojo.map( data, 'return item[1]' );
    var users     = dojo.map( authors[0], 'return item[0]' );
    var cpdata    = makechart( authors );
    var series    = cpdata[0];
    series[series.length] = { type: 'pie',
                              name: 'Total edits by authors',
                              data: cpdata[1],
                              center: ['80%', '10%'],
                              size: 100,
                              showInLegend: false
                            }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            zoomType: 'x',
            margin: [ 50, 50, 120, 80]
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            categories: wikipages,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { 
                text: 'Count',
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        tooltip: {
            formatter: function() {
                var s;
                if (this.point.name) { // the pie chart
                    s = '<b>' + this.point.name + '</b>,<br/>' + 'edited ' + this.y + ' times'
                } else {
                    s = '<b>' + this.series.name + '</b>,<br/>' + 'edited ' + this.y + ' times'
                }
                return s;
            }
        },
        labels: {
        },
        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },
        series: series
    });
    return chart;
}

function chart19_wikicommentors( data, id ) {
    function makedata( commentors, i ) {
        var data  = [];
        var total = 0;
        for(j = 0; j < commentors.length; j++) {
            data[data.length] = commentors[j][i][1];
            total += commentors[j][i][1]; 
        }
        return [ data, total ]
    }
    function makechart( commentors ) {
        var wseries = [];
        var utotal  = [];
        for(i = 0; i < commentors[0].length; i++ ) {
            var username = commentors[0][i][0];
            var values   = makedata( commentors, i );
            wseries[wseries.length] = {
                    type : 'column',
                    name : username,
                    data : values[0]
            }
            utotal[utotal.length] = {
                    name : username,
                    y    : values[1]
            }
        }
        return [ wseries, utotal ]
    }

    var wikipages = dojo.map( data, 'return item[0]' );
    var commentors= dojo.map( data, 'return item[1]' );
    var users     = dojo.map( commentors[0], 'return item[0]' );
    var cpdata    = makechart( commentors );
    var series    = cpdata[0];
    series[series.length] = { type: 'pie',
                              name: 'Total comments',
                              data: cpdata[1],
                              center: ['80%', '5%'],
                              size: 100,
                              showInLegend: false
                            }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            zoomType: 'x',
            margin: [ 50, 50, 200, 80]
        },
        title: { text: '' },
        subtitle: { text: ''},
        xAxis: {
            categories: wikipages,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { 
                text: 'Count',
            }
        },
        legend: {
            style: {
                left: '20px',
                bottom: '10px',
                right: 'auto',
                top: 'auto'
            },
            itemStyle: { fontSize : 'small' }
        },
        tooltip: {
            formatter: function() {
                var s;
                if (this.point.name) { // the pie chart
                    s = '<b>' + this.point.name + ',</b><br/>' + 'commented ' + this.y + ' times'
                } else {
                    s = '<b>' + this.series.name + ',</b><br/>' + 'commented ' + this.y + ' times'
                }
                return s;
            }
        },
        labels: {
            //items: [{
            //    html: 'Total comments',
            //    style: {
            //        left: '140px',
            //        top: '0px',
            //        color: 'black'				
            //    }
            //}]
        },
        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },
        series: series
    });
    return chart;
}

function chart20_wiki_vs_tags( data, id ) {
    var wiki_no = dojo.map( data, "return item[1].length" );
    var tagnames  = dojo.map( data, "return item[0]" );
    var filenames = function( wikis ) {
                        return dojo.map( wikis, "return item[1]" );
                    }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'column',
            zoomType: 'x',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: 'Wikipages by tagname' },
        subtitle: { text: 'Click and drag in the plot area to zoom in'},
        xAxis: {
            title: { text: 'Tagname' },
            tickInterval: 1,
            labels: {
                formatter: function() { return tagnames[this.value] },
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { text: 'No. of wikipages' }
        },
        tooltip: {
            formatter: function() {
                    return '<b>'+ data[this.x][0] + '</b><br/>' +
                           filenames( data[this.x][1] ).join( '<br/>' )
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            column: {
                dataLabels: {
                    formatter: function() { return this.y },
                    enabled : true,
                    style: {
                        color: '#FFFFFF'
                    }
                }
            }
        },
        series: [{
            name: 'tagged wikipages',
            data: wiki_no
        }]
    });
    return chart;
}

/*************************** Ticket Charts ******************************/

function chart21_projtickets( data, id ) {
    var piedata = [{ name : 'type',
                     data : data[0],
                     center: ["10%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'status',
                     data : data[1],
                     center: ["48%", "90%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'severity',
                     data : data[2],
                     center: ["86%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }]

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        legend: {
            enabled: false
        },
        labels: {
            items: [{
                html: '',
                style: {
                    left: '10px',
                    top: '0px',
                    color: 'crimson'				
                }
            }, {
                html: '',
                style: {
                    left: '210px',
                    top: '0px',
                    color: 'crimson'
                }
            }, {
                html: '',
                style: {
                    left: '430px',
                    top: '0px',
                    color: 'crimson'
                }
            }]
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.point.name;
                    },
                    color: '#111',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif',
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return'<b>' + this.point.name + ',<b><br/>' + this.y;
            }
        },
        series: piedata
    });
    return chart;
}

function chart22_ticketowners( data, id ) {
    var piedata = [{ name : 'type',
                     data : data[0],
                     center: ["10%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'status',
                     data : data[1],
                     center: ["48%", "90%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'severity',
                     data : data[2],
                     center: ["86%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }]
    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        legend: {
            enabled: false
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.point.name;
                    },
                    color: '#111',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return'<b>' + this.point.name + ',<b><br/>' + this.y;
            }
        },
        series: piedata
    });
    return chart;
}

function chart23_ticketcomponents( data, id ) {
    var piedata = [{ name : 'type',
                     data : data[0],
                     center: ["10%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'status',
                     data : data[1],
                     center: ["48%", "90%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'severity',
                     data : data[2],
                     center: ["86%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }]

    console.log(arguments);
    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        legend: {
            enabled: false
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.point.name;
                    },
                    color: '#111',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return'<b>' + this.point.name + ',<b><br/>' + this.y;
            }
        },
        series: piedata
    });
    return chart;
}

function chart24_ticketmilestones( data, id ) {
    var piedata = [{ name : 'type',
                     data : data[0],
                     center: ["10%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'status',
                     data : data[1],
                     center: ["48%", "90%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'severity',
                     data : data[2],
                     center: ["86%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }]

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        legend: {
            enabled: false
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.point.name;
                    },
                    color: '#111',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return'<b>' + this.point.name + ',<b><br/>' + this.y;
            }
        },
        series: piedata
    });
    return chart;
}

function chart25_ticketversions( data, id ) {
    var piedata = [{ name : 'type',
                     data : data[0],
                     center: ["10%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'status',
                     data : data[1],
                     center: ["48%", "90%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'severity',
                     data : data[2],
                     center: ["86%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }]

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        legend: { enabled: false },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return this.point.name;
                    },
                    color: '#111',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return'<b>' + this.point.name + ',<b><br/>' + this.y;
            }
        },
        series: piedata
    });
    return chart;
}

function chart26_ticketcommentors( data, id ) {
    function makedata( commentors, i ) {
        var data  = [];
        var total = 0;
        for(j = 0; j < commentors.length; j++) {
            data[data.length] = commentors[j][i][1];
            total += commentors[j][i][1]; 
        }
        return [ data, total ]
    }
    function makechart( commentors ) {
        var wseries = [];
        var utotal  = [];
        for(i = 0; i < commentors[0].length; i++ ) {
            var username = commentors[0][i][0];
            var values   = makedata( commentors, i );
            wseries[wseries.length] = {
                    type : 'column',
                    name : username,
                    data : values[0]
            }
            utotal[utotal.length] = {
                    name : username,
                    y    : values[1]
            }
        }
        return [ wseries, utotal ]
    }

    var tickets   = dojo.map( data, 'return item[0]' );
    var commentors= dojo.map( data, 'return item[1]' );
    var users     = dojo.map( commentors[0], 'return item[0]' );
    var cpdata    = makechart( commentors );
    var series    = cpdata[0];
    series[series.length] = { type: 'pie',
                              name: 'Total comments',
                              data: cpdata[1],
                              center: ['80%', '5%'],
                              size: 100,
                              showInLegend: false
                            }

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            zoomType: 'x',
            margin: [ 50, 50, 200, 80]
        },
        title: { text: '' },
        xAxis: {
            categories: tickets,
            labels: {
                rotation: -45,
                align: 'right',
                style: {
                     font: 'normal 13px Verdana, sans-serif'
                }
            },
            maxZoom: 10
        },
        yAxis: {
            title: { 
                text: 'Count',
            }
        },
        legend: {
            style: {
                left: '20px',
                bottom: '10px',
                right: 'auto',
                top: 'auto'
            },
            itemStyle: { fontSize : 'small' }
        },
        tooltip: {
            formatter: function() {
                var s;
                if (this.point.name) { // the pie chart
                    s = '<b>' + this.point.name + ',</b><br/>' + 'commented ' + this.y + ' times'
                } else {
                    s = '<b>' + this.series.name + ',</b><br/>' + 'commented ' + this.y + ' times'
                }
                return s;
            }
        },
        labels: {
        },
        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },
        series: series
    });
    return chart;
}

/*************************** Review Charts ******************************/

function chart27_reviewusers( data, id ) {
    var piedata = [{ name : 'author',
                     data : data[0],
                     center: ["10%", "30%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'moderator',
                     data : data[1],
                     center: ["48%", "90%"],
                     size: "80%",
                     showInLegend: false
                  }, {
                     name : 'participant',
                     data : data[2],
                     center: ["86%", "30%"],
                     size: "80%",
                  }]

    hc_setoption();
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'pie',
            margin: [ 50, 50, 100, 80]
        },
        title: { text: '' },
        labels: {
        },
        legend: {
            enabled: false,
            layout: 'vertical',
            style: {
                left: '50px',
                bottom: 'auto',
                right: 'auto',
                top: '100px'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                dataLabels: {
                    enabled: false,
                    formatter: function() {
                        return this.point.name;
                    },
                    color: 'white',
                    style: {
                        font: '13px Trebuchet MS, Verdana, sans-serif'
                    }
                }
            }
        },
        tooltip: {
            formatter: function() {
                return'<b>' + this.point.name + ',<b><br/>' + this.y;
            }
        },
        series: piedata
    });
    return chart;
}

/*************************** Timeline Charts ******************************/

function timelinechart( datatline, fromdate, id, title ) {
    var counttline = dojo.map( datatline, "return item.length" );
    var itemlogs   = function ( logs ) {
                        return dojo.map( logs, "return item[2]" ) };

    hc_setoption('dark-green');
    chart = new Highcharts.Chart({
        chart: {
            renderTo: id,
            defaultSeriesType: 'areaspline',
            zoomType: 'x',
            margin: [ 50, 50, 50, 80]
        },
        title: {
            text: title
        },
        subtitle: {
            text: 'Click and drag in the plot area to zoom in'
        },
        xAxis: {
            type: 'datetime',
            maxZoom: 10*24*3600000, // Ten days
        },
        yAxis: {
            title: { text: 'Acitivity' },
            startOnTick: false,
            showFirstLable: false,
        },
        tooltip: {
            formatter: function() {
                    var offset = (this.x-fromdate) / 3600 / 1000 / 24;
                    return '<b> on '+ new Date(this.x).toDateString() +'</b><br/>' + 
                           datatline[offset].length + ' activities';
            }
        },
        legend: {
            align: "left", verticalAlign: "top", x: 5, y: 5,
            itemStyle: { fontSize : 'small' }
        },
        plotOptions: {
            areaspline: {
                fillOpacity: 0.5,
                lineWidth: 1,
                marker: {
                    enabled: true,
                    radius: 1,
                    states: {
                        hover: { enabled: true, radius: 3 }
                    }
                },
                shadow: false,
                states: {
                    hover: { lineWidth: 1 }
                }
            }
        },
        series: [{
            name: title,
            pointInterval: 24 * 3600 * 1000,
            pointStart: fromdate,
            data: counttline
        }]
    });
    return chart
}
