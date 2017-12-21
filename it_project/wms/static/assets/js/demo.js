type = ['', 'info', 'success', 'warning', 'danger'];


demo = {
    initPickColor: function() {
        $('.pick-class-label').click(function() {
            var new_class = $(this).attr('new-class');
            var old_class = $('#display-buttons').attr('data-class');
            var display_div = $('#display-buttons');
            if (display_div.length) {
                var display_buttons = display_div.find('.btn');
                display_buttons.removeClass(old_class);
                display_buttons.addClass(new_class);
                display_div.attr('data-class', new_class);
            }
        });
    },


initWaterLevel: function(latest) {

        /* ----------==========     Daily Sales Chart initialization    ==========---------- */
        var x = latest.splice(0,14);
        x = x.reverse();

        dataLevelChart = {
            labels: ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th'],
            series: [
                x.map(v => v.level).splice(0, 14)
            ]
        };

        optionsLevelChart = {
            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),
            low: 0,
            high: 100, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            },
        }

        var levelChart = new Chartist.Line('#levelChart', dataLevelChart, optionsLevelChart);

        md.startAnimationForLineChart(levelChart);

},






    initDashboardPageCharts: function(latest) {

        /* ----------==========     Daily Sales Chart initialization    ==========---------- */
        var x = latest.splice(0,14);
        x = x.reverse();

        dataTemperatureChart = {
            labels: ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th'],
            series: [
                x.map(v => v.temperature).splice(0, 14)
            ]
        };

        optionsTemperatureChart = {
            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),
            low: 0,
            high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            },
        }

        var temperatureChart = new Chartist.Line('#temperatureChart', dataTemperatureChart, optionsTemperatureChart);

        md.startAnimationForLineChart(temperatureChart);



        /* ----------==========     Completed Tasks Chart initialization    ==========---------- */

        dataHumidityChart = {
            labels: ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th'],
            series: [
                x.map(v => v.humidity).splice(0, 14)
            ]
        };

        optionsHumidityChart = {
            lineSmooth: Chartist.Interpolation.cardinal({
                tension: 0
            }),
            low: 0,
            high: 100, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
            chartPadding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            }
        }

        var humidityChart = new Chartist.Line('#humidityChart', dataHumidityChart, optionsHumidityChart);

        // start animation for the Completed Tasks Chart - Line Chart
        md.startAnimationForLineChart(humidityChart);


        /* ----------==========     Emails Subscription Chart initialization    ==========---------- */

        var dataSoilChart = {
            labels: ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th'],
            series: [
                x.map(v => v.soilMoisture).splice(0, 14)

            ]
        };
        var optionsSoilChart = {
            axisX: {
                showGrid: false
            },
            low: 0,
            high: 100,
            chartPadding: {
                top: 0,
                right: 5,
                bottom: 0,
                left: 0
            }
        };
        var responsiveOptions = [
            ['screen and (max-width: 640px)', {
                seriesBarDistance: 5,
                axisX: {
                    labelInterpolationFnc: function(value) {
                        return value[0];
                    }
                }
            }]
        ];
        var soilChart = Chartist.Bar('#soilChart', dataSoilChart, optionsSoilChart, responsiveOptions);

        //start animation for the Emails Subscription Chart
        md.startAnimationForBarChart(soilChart);

    }

}
