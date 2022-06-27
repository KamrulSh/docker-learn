console.log('Hello Javascript')


odoo.define('effort_timesheet.colorcalendar', function (require) {
    "use strict";
    console.log('cal1 dayRender')

    const CalendarRenderer = require('web.CalendarRenderer');
    var CalendarModelCustom = CalendarRenderer.extend({

        start: function () {
            console.log("START FUNCTION")
            var self = this;
            return this._super().then(function () {
                self.dayRender();
            });
        },

        dayRender: function (date, cell) {
            console.log('calling dayRender')
            var today = new Date();
            if (date.getDate() === today.getDate()) {
                cell.css("background-color", "red");
            }
        }
    });


    return CalendarModelCustom;

});