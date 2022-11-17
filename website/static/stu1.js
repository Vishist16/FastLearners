
$(document).ready(function(){
    load_data();
    function load_data(query='')
    {
        $.ajax({
            url:"/subtoprecords",
            method:"POST",
            data:{query:query},
            success:function(data)
            { 
                $('tbody').html(data);
                $('tbody').append(data.htmlresponse);
            }
        })
    }
 
    $('#search_filter2').change(function(){
        $('#hidden_value2').val($('#search_filter2').val());
        var query = $('#hidden_value2').val(); 
        load_data(query);
    });
     
});
