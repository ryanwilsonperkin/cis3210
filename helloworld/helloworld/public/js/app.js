/* Globally accessible Links agent. */
var linksAgent;

/* Load clippy js. */
clippy.load('Links', function(agent) {
    linksAgent = agent;
    agent.show();

    /* Register actions to select dropdown. */
    $.each(linksAgent.animations(), function(index, animation) {
        $('#animation-list').append(
            $('<option></option>').val(animation).html(animation)
        );
    });

    /* Trigger play on click of animate button. */
    $('#animate').click(function() {
        linksAgent.play($('#animation-list').val());
    });

    /* Trigger speaking on click of say-hello button. */
    $('#say-hello').click(function() {
        linksAgent.speak($('#links-text').val());
    });
});
