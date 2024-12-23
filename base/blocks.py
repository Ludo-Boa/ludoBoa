from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    BooleanBlock,
    DateBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtailcodeblock.blocks import CodeBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock


class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Choisir la taille du titre"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow", features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough' ], template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        template="blocks/embed_block.html",
        
    )
    table_block = TableBlock()
    code_block = CodeBlock(label='Code')


COLOR_CHOICE = {
    "Yellow": "#f9e300",
    "DodgerBlue": "#2d72ff",
    "Purple": "#800080",
    "MediumPurple": "#9574ce",
    "DarkGreen": "#0a753a",
    "OrangeRed": "#ee4d00 ",
    "LightSkyBlue": "#8aa9f9",
    "DeepPink": "#8aa9f9",
}


class EducationBlock(StructBlock):
    title = CharBlock(label="Titre", classname="title", required=True)
    bg_color = ChoiceBlock(help_text="Sélectionner la couleur de fond du titre", required=True, choices=[
        ("f9e300", "Yellow"),
        ("2d72ff", "DodgerBlue"),
        ("800080", "Purple"),
        ("9574ce", "MediumPurple"),
        ("0a753a", "DarkGreen"),
        ("ee4d00 ", "OrangeRed"),
        ("8aa9f9", "LightSkyBlue"),
        ("e20d87", "DeepPink", ),
    ])
    school = CharBlock(label="Ecole", classname="school", required=True)
    city = CharBlock(label="Ville", classname="city", required=True)
    date_start = DateBlock(label="Date de début")
    date_end = DateBlock(label="Date de fin", required=False)
    level = ChoiceBlock(
        choices=[
            ("", "Selectionnez un niveau"),
            ("cap", "CAP"),
            ("bep", "BEP"),
            ("bac", "BAC"),
            ("bac+2", "BAC+2"),
            ("bac+3", "BAC+3"),
            ("bac+4", "BAC+4"),
            ("bac+5", "BAC+5"),
            ("bac+8", "BAC+8"),
        ],
        blank=True,
        required=False,
        label="Niveau",
    )
    certificate = BooleanBlock(label="Diplôme", required=False, help_text="cocher la case si le diplôme a été obtenu")
    description = RichTextBlock(
        label="Description",
        icon="pilcrow", 
        features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough' ], 
        required=False, 
        template="blocks/paragraph_block.html"
    )

    class Meta:
        template = "blocks/education_block.html"



class ResumeStreamBlock(StreamBlock):
    education_block = EducationBlock()



class ExperienceBlock(StructBlock):
    title = CharBlock(label="titre", classname="title", required=True)
    bg_color = ChoiceBlock(help_text="Sélectionner la couleur de fond du titre", required=True, choices=[
        ("f9e300", "Yellow"),
        ("2d72ff", "DodgerBlue"),
        ("800080", "Purple"),
        ("9574ce", "MediumPurple"),
        ("0a753a", "DarkGreen"),
        ("ee4d00 ", "OrangeRed"),
        ("8aa9f9", "LightSkyBlue"),
        ("e20d87", "DeepPink", ),
    ])
    company = CharBlock(label="entreprise", classname="company", required=True)
    city = CharBlock(label="ville", classname="city", required=True)
    date_start = DateBlock()
    date_end = DateBlock(required=False)
    description = RichTextBlock(
        icon="pilcrow", features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough' ], required=False, template="blocks/paragraph_block.html"
    )

    class Meta:
        template = "blocks/experience_block.html"



class ExperienceStreamBlock(StreamBlock):
    experience_block = ExperienceBlock() 