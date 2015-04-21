/**
 * Created by gep on 4/17/15.
 */

$(function(){
//    SyntaxHighlighter.all();

    var progressBar = $('#progress-bar'),
        alertContainer = $('div.alert-danger'),
        errorMessageContainer = $('#errorMessage'),
        successAlertContainer = $('div.alert-success'),
        wellContainer = $('div.well'),
        codeContainer = $('pre#code-container');

    $('#main-form').submit(function(){
        var form = $(this);
        progressBar.show();
        codeContainer.hide();
        $('div#code-container').remove();
        codeContainer = $('pre#code-container');
        if (codeContainer.length == 0){
            wellContainer.append(
                $('<pre id="code-container" style="display: none" class="brush: html; highlight: "></pre>')
            );
            codeContainer = $('pre#code-container');
        }
        alertContainer.addClass('hide');
        successAlertContainer.addClass('hide');
        $.ajax({
            url: form.attr('action') + '?' + form.serialize(),
            success: function(data){
                progressBar.hide();
                errorMessageContainer.text('');
                if (data.errors && data.errors instanceof Object && !$.isEmptyObject(data.errors)){
                    alertContainer.removeClass('hide');
                    for (key in data.errors){
                        errorMessageContainer.text(
                                errorMessageContainer.text() + key + ': ' + data.errors[key] + ' '
                        );
                    }
                    return false;
                }

                if ($.isEmptyObject(data.occurrences)){
                    successAlertContainer.removeClass('hide');
                    return false;
                }

                alertContainer.removeClass('hide');
                errorMessageContainer.text('Cyrillic symbols found! Lines with cyrillic characters are highlighted.');
                codeContainer.attr('class', codeContainer.attr('class') + '[');
                $.each(data.occurrences, function(line){
                    codeContainer.attr('class', codeContainer.attr('class') + line + ',');
                });
                codeContainer.attr('class', codeContainer.attr('class') + ']');
                codeContainer.show();
                codeContainer.html(data.html);
//                codeContainer.find('code').html(data.html);
//                Prism.highlightAll();
                SyntaxHighlighter.highlight();
            }
        });
        return false;
    });

});


