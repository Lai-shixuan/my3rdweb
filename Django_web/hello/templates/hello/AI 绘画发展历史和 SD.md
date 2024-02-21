主要（整篇）参考文献：

# 1. AI 绘画发展历史

主流模型包括
1. DALL·E2, Open AI 公司开发的, 2022.4 月上线, 至少基于 gpt-3, 且可以和 gpt-4 联合使用[^1]
2. Stable diffusion (SD), Stability. ai 公司开发的, 2022.7 月上线, 也可以联合使用, 基于 diffusion 模型。该公司发布了一个网站叫 clipdrop，基础功能包括抠图、去除杂物等，开会员可以使用生成图的功能
3. Midjourney, Midjourney inc 开发的，在 discord 平台, 2022.3 月上线, 基于 diffusion。在 discord 上进行使用

novelai 是更早开发的模型，但是目前也基于 stable diffusion 开发，专精于动漫画风[^2]。

# 2. Stable diffusion

和 Midjourney 不同，SD 更多像一个框架，因此有非常多的模型在 C 站上进行发布。SD 的历史包括 1.0，2.0，XL，XL turbo，和 23 年年底发布的 stable cascade[^4]。

模型相关的名词解释详见下图，来源详见[^3]
![](attachment/aa1bf7b4ede9f8e36b4f56cbfbfcaaa1.png)

![](attachment/e91aae83f56042e86de8ef522dff5f86.png)
之所以 SD 被称为大模型，是为了和微调后的模型区分。微调模型主要是玩家们自己调整的，可以将微调的部分单独拆出来形成 lora 等，也可以直接基于大模型进行微调，并将所有参数分享出来形成一个新的大模型

在使用方面，SD 可以用纯粹的 1) python 程序，2) Web UI，3）ComfyUI 进行使用，webUI 是非常直观的输入参数和生成图片，有很多的按钮和参数选择，而 comfyUI 更多关注流程，因此便于将出图的流程分享出去。注意，UI 进行的只有 UI 界面，模型要自己下载和自己使用，UI 应该具备训练功能但是我没有使用过。Web UI 有国内开发的整合包。

[^1]: [did dall·e based on gpt-4 - Google Search](https://www.google.com/search?q=did+dall%C2%B7e+based+on+gpt-4&newwindow=1&sxsrf=AB5stBjKwVNJc6c63LFC_li766K7KtMd0g%3A1688546637939&ei=TS2lZOH4OMTP-QbqtpuIBw&ved=0ahUKEwih06m0lvf_AhXEZ94KHWrbBnEQ4dUDCBA&uact=5&oq=did+dall%C2%B7e+based+on+gpt-4&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCCEQoAEyBQghEKABMgUIIRCgATIFCCEQoAEyBQghEKABMggIIRAWEB4QHToHCCMQigUQJzoICAAQigUQkQI6BwgAEIoFEEM6BwguEIoFEEM6BQgAEIAEOgUILhCABDoECAAQHjoICAAQgAQQywE6BwgAEIAEEAo6BwghEKABEAo6BggAEBYQHjoKCCEQFhAeEA8QHToECCEQFUoECEEYAFAAWIt1YPR1aAlwAXgBgAGkA4gBlhySAQoyLjI0LjEuMC4xmAEAoAEBwAEB&sclient=gws-wiz-serp)
[^2]: [novelai和stable diffusion有什么区别？一文讲透stable diffusion和novelai的关系 - 画宇宙](https://www.nolibox.com/creator_articles/difference_between_novelai_and_stablediffusion.html)
[^3]: [【AI绘图】入门必看 C站模型下载与使用指南 | 底模型+微调模型+VAE模型+关键词 | 模型文件名与后缀名详解 | Stable Diffusion\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV19L411676Z/?spm_id_from=333.337.search-card.all.click&vd_source=0a51168ae036ea20f779efa5283cd30b)
[^4]: [Stable Diffusion - Wikipedia](https://en.wikipedia.org/wiki/Stable_Diffusion#Releases)