var F="flex",N="none";
function midVisible()
{
    document.querySelector("#middle_cards").style.display=F;
    document.querySelector("#left_cards").style.display=N;
}
function leftVisible()
{
    document.querySelector("#middle_cards").style.display=N;
    document.querySelector("#left_cards").style.display=F;
}
document.querySelector("#blogs").addEventListener("click",midVisible);
document.querySelector("#research").addEventListener("click",leftVisible);