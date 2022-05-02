# time and background tasks
import asyncio
# discord libs
import hikari
import lightbulb
from lightbulb import commands

from commands.errors.time_format import checkTimeFormat
from commands.errors.errors import IncorrectTimeFormat

# The options the command will have.
@lightbulb.option("duration", "The duration of the poll (like 05:30 [mm:ss]).",
    str, required=True)
@lightbulb.option("question", "The question/subject of the poll.", str,
    required=True)
@lightbulb.option("opt1", "The first possible option.", str, required=True)
@lightbulb.option("opt2", "The second possible option.", str, required=True)
@lightbulb.option("opt3", "The third possible option.", str, required=False)
@lightbulb.option("opt4", "Fourth possible option.", str, required=False)
@lightbulb.option("opt5", "Fifth possible option.", str, required=False)
@lightbulb.option("opt6", "Sixth possible option.", str, required=False)
@lightbulb.option("opt7", "Seventh possible option.", str, required=False)
@lightbulb.option("opt8", "Eighth possible option.", str, required=False)
@lightbulb.option("opt9", "Ninth possible option.", str, required=False)
@lightbulb.option("opt10", "Tenth possible option.", str, required=False)
# Convert the function into a command
@lightbulb.command("poll", "Create a poll.")
# Define the types of command that this function will implement
@lightbulb.implements(commands.PrefixCommand, commands.SlashCommand)
async def poll(ctx: lightbulb.context.Context) -> None:
    ## retrieve args ##
    duration = ctx.options._options["duration"]
    question = ctx.options._options["question"]
    i = 1
    list_opt = []
    #TODO: max legnth for 1 opt is 80 chars
    for opt in ctx.options._options:
        try:
            if ctx.options._options[f"opt{i}"] != None:
                list_opt += [ctx.options._options[f"opt{i}"]]
        except KeyError:
            break
        i += 1
    ## set up duration ##
    # handle incorrect format
    if checkTimeFormat(duration) == False:
        resp = await ctx.respond(content=IncorrectTimeFormat(duration).message)
        await resp.message()
        return
    to_wait = convertTime(duration)
    ## build embed ##
    embed = hikari.Embed(title=f"{question}", description="",
            colour=hikari.Colour(0x563275),)
    embed.set_author(name=f"Vote duration: {to_wait}sec")
    embed.set_footer(
        text=f"Requested by {ctx.member.display_name}",
        icon=ctx.member.avatar_url,
    )
    # add a field for each event
    i = 1
    for opt in list_opt:
        embed.add_field(name=f"`{opt}`", value=f"`{i}`")
        i += 1
    ## add buttons ##
    row = ctx.app.rest.build_action_row()
    # you can add up to 5 buttons for one row,
    # so if there is more than 5 options, we add another row
    if len(list_opt) > 5:
        row2 = ctx.app.rest.build_action_row()
    else:
        row2 = None
    i = 1
    # build a button for each option
    for opt in list_opt:
        if i <= 5:
            (
                row.add_button(hikari.ButtonStyle.PRIMARY, f"{i}")
                .set_label(f"{opt}")
                .add_to_container()
            )
        if i > 5:
            (
                row2.add_button(hikari.ButtonStyle.PRIMARY, f"{i}")
                .set_label(f"{opt}")
                .add_to_container()
            )
        i += 1
    ## send response ##
    if row2 != None:
        resp = await ctx.respond(embed=embed, components=[row, row2,])
    else:
        resp = await ctx.respond(embed=embed, components=[row,])
    msg = await resp.message()
    ## wait the desired time to handle votes ##
    # await asyncio.sleep(to_wait)
    ## accounting of votes ##
    #TODO: accounting votes
    ## send result ##


def convertTime(duration: str) -> int:
    """Convert the time passed in argument (like mm:ss) into seconds.

    Args:
        `duration`(str): The duration to convert into seconds.

    Returns:
        `int`: The duration converted into seconds.
    """
    if duration.find(":") == -1:
        return int(duration)
    else:
        min = duration.split(":")[0]
        sec = duration.split(":")[1]
        return (int(min)*60 + int(sec))


def load(bot: lightbulb.BotApp) -> None:
    bot.command(poll)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_command(bot.get_slash_command("poll"))