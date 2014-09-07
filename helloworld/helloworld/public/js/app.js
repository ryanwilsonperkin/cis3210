/* Globally accessible Links agent. */
var linksAgent;

/* Load clippy js. */
clippy.load('Links', function(agent) {
    linksAgent = agent;
    agent.show();
});

/* Register actions to buttons. */
$('#animate').click(function() {
    linksAgent.animate();
});

$('#say-hello').click(function() {
    linksAgent.speak('Hello!');
});
