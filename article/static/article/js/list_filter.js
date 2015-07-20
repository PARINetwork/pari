var ListFilter = {
    init: function() {
        $('.type-filter').on('click', $.proxy(function(event){
            var filterElement = $(event.target).parent('.type-filter');
            if(filterElement.hasClass('active')){
                this.listContainer.data('filter-args-filter', null);
            } else {
                this.listContainer.data('filter-args-filter', filterElement.data('filter'));
            }
            this.listContainer.data('filter-args-page', 1);
            this.collectArgsAndSumbit();
        }, this));

        $('[data-page]').on('click', $.proxy(function(event){
            event.preventDefault();
            var paginationElement = $(event.target).closest('li');

            this.listContainer.data('filter-args-page', paginationElement.data('page'));

            this.collectArgsAndSumbit();
        }, this));

        $('.view-all').on('click', $.proxy(function(event){
            $('.type-filters').addClass('expanded');
            target = $(event.target);
            target.hide();
        }, this));

        this.callbackInit();
    },

    updateHistory: function(args){
        this.historyFlag = false;
        var paramArgs = $.param(args);
        History.pushState(args, 
            this.listContainer.data('title') + (args['filter'] ? ' - ' + args['filter'] : ""), 
            paramArgs === "" ? null : "?" + paramArgs);
    },

    collectArgsAndSumbit: function(){
        var nonRequiredArgs = this.collectNonRequiredArgs();
        this.submit(nonRequiredArgs);
    },

    collectNonRequiredArgs: function(){
        var filterArgsPrefix = "filterArgs";
        return this.collectArgs(filterArgsPrefix);
    },

    collectRequiredArgs: function(){
        var filterArgsPrefix = "filterRequiredArgs";
        return this.collectArgs(filterArgsPrefix);
    },

    collectArgs: function(argsPrefix){
        var args = {};

        $.each(this.listContainer.data(), function(key,value){
            if(value != null && key.substring(0, argsPrefix.length) === argsPrefix){
                var arg = key.replace(argsPrefix,'').toLowerCase();
                args[arg] = value;
            }
        });

        return args;
    },

    historyBind: function(){
        History.Adapter.bind(window,'statechange',$.proxy(function(){
            if(this.historyFlag){
                var State = History.getState();
                var filterEndpoint = this.listContainer.data('filter-endpoint');
                this.submit(State.data);
            }
            this.historyFlag = true;
        }, this));
    },

    submit: function(nonRequiredArgs){
        this.updateHistory(nonRequiredArgs);
        var requiredArgs = this.collectRequiredArgs();
        var args = $.extend({}, nonRequiredArgs, requiredArgs);
        var filterEndpoint = this.listContainer.data('filter-endpoint');
        Dajaxice.pari.article[filterEndpoint](Dajax.process, args);
        this.callbackInit();

    },

    callbackInit: function() {
        $('[data-toggle="tooltip"]').tooltip();
    },

    historyFlag: true,

    listContainer: $('.filter-list-container')
}

$(function(){
    ListFilter.init();
    ListFilter.historyBind();
});